import yaml
from pathlib import Path
from docgen.data_fetcher import DataFetcher
from docgen.entities import Project, create_workers_from_map
from docgen.generators import generate_act, generate_task, generate_statement
from docxtpl import DocxTemplate
from typing import Dict

def load_config():
    with open(Path(__file__).parent.parent / "config.yaml", "r") as f:
        return yaml.safe_load(f)    

def get_projects(settings) -> Dict:
    fetcher = DataFetcher(settings.get("api_token"), settings.get("worker_table_path"))
    projects = fetcher.get_projects()

    d = {}

    for p in projects:
        d[p["name"]] = p["id"]

    return d


def generate_acts(project: Project, settings):
    '''Генерация актов.'''
    for w in project.workers:
        doc = DocxTemplate(settings.get("act_template_path"))
        generate_act(doc, project, w)
        doc.save(settings.get("output_dir") + "act_{}.docx".format(w.initials()))

def generate_tasks(project: Project, settings):
    '''Генерация задания.'''
    doc = DocxTemplate(settings.get("task_template_path"))
    generate_task(doc, project)
    doc.save(settings.get("output_dir") + "task_{}.docx".format(project.font.name_and_version()))

def generate_statements(project: Project, settings):
    '''Генерация заверения.'''
    doc = DocxTemplate(settings.get("statement_template_path"))
    generate_statement(doc, project)
    doc.save(settings.get("output_dir") + "statement_{}.docx".format(project.font.name_and_version()))

def get_project_data(project_name: str, settings) -> Project:
    '''Получение данных и формирование проекта.'''
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
