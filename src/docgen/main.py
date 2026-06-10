import yaml
from pathlib import Path
from docgen.data_fetcher import DataFetcher
from docgen.utils.utils import find_max_full_name
from docgen.entities import Project, Font, create_workers_from_map
from docgen.generators import generate_act, generate_task, generate_statement
from docxtpl import DocxTemplate
from typing import Dict

def load_config():
    with open(Path(__file__).parent.parent / "config.yaml", "r") as f:
        return yaml.safe_load(f)

# config = load_config()
# fetcher = DataFetcher(config["api"]["token"], config["resources"]["worker_table_path"])    

def get_projects(settings) -> Dict:
    fetcher = DataFetcher(settings.get("api_token"), settings.get("worker_table_path"))
    projects = fetcher.get_projects()

    d = {}

    for p in projects:
        d[p["name"]] = p["id"]

    return d

def demo_gengerate(project_name: str, style: str, glyph_path: str):
    fetcher = DataFetcher(config["api"]["token"], config["resources"]["worker_table_path"])
    workers_mapping = fetcher.get_workers_mapping()

    workers_data = fetcher.get_workers_data()
    projects = fetcher.get_projects()
    
    for p in projects:
        if p["name"] == project_name:
            proj = p
            break

    project_info = fetcher.get_project_info(proj["id"])
    workers = create_workers_from_map(project_info["authors"], workers_data, workers_mapping)
    font = Font(file_or_path=config["project"]["glyph_file_path"])
    print("Проект", font.name_and_version())

    print("Кто руководитель проекта:")
    for i, w in enumerate(workers):
        print(f'{i}. {w.full_name()}')

    h_index = int(input("Введите номер руководителя: "))
    print("Выбран руководитель: ", workers[h_index].full_name())

    project = Project(
            work_name=proj["name"],
            final_name=config["project"]["final_name"],
            start=project_info["start_date"],
            end=project_info["end_date"],
            style=config["project"]["style"],
            workers=workers,
            font=font,
            head=workers[h_index]
            )

    #Generation of acts
    if input("Генерируем акт? (Y/N): ") == "Y":
        print("Генерируем акты...")
        for w in project.workers:
            doc = DocxTemplate(config["templates"]["act_template_path"])
            generate_act(doc, project, w)
            doc.save(config["output"]["act_path"] + "act_{}.docx".format(w.initials()))

    #Generation of task
    if input("Генерируем задание? (Y/N): ") == "Y":
        doc = DocxTemplate(config["templates"]["task_template_path"])
        generate_task(doc, project)
        doc.save(config["output"]["task_path"] + "task_{}.docx".format(project.font.name_and_version()))

    if input("Генерируем ведомость? (Y/N): ") == "Y":
        max_length = find_max_full_name(project.workers)
        doc = DocxTemplate(config["templates"]["statement_template_path"])
        generate_statement(doc, project, max_length)
        doc.save(config["output"]["statement_path"] + "statement_{}.docx".format(project.font.name_and_version()))

    print("Готово!")


def generate_acts(project: Project, settings):
    for w in project.workers:
        doc = DocxTemplate(settings.get("act_template_path"))
        generate_act(doc, project, w)
        doc.save(settings.get("output_dir") + "act_{}.docx".format(w.initials()))

def generate_tasks(project: Project, settings):
    doc = DocxTemplate(settings.get("task_template_path"))
    generate_task(doc, project)
    doc.save(settings.get("output_dir") + "task_{}.docx".format(project.font.name_and_version()))

def generate_statements(project: Project, settings):
    doc = DocxTemplate(settings.get("statement_template_path"))
    generate_statement(doc, project)
    doc.save(settings.get("output_dir") + "statement_{}.docx".format(project.font.name_and_version()))

def get_project_data(project_name: str, settings) -> Project:
    fetcher = DataFetcher(settings.get("api_token"), settings.get("worker_table_path"))
    workers_mapping = fetcher.get_workers_mapping()

    workers_data = fetcher.get_workers_data()
    
    projects = fetcher.get_projects()
    
    for p in projects:
        if p["name"] == project_name:
            proj = p
            break

    project_info = fetcher.get_project_info(proj["id"])

    workers = create_workers_from_map(project_info["authors"], workers_data, workers_mapping)

    # font = Font(file_or_path=glyph_path)

    project = Project(
        work_name=proj["name"],
        final_name=None,
        start=project_info["start_date"],
        end=project_info["end_date"],
        style=None,
        workers=workers,
        font=None,
        head=workers[0]
        )

    return project
