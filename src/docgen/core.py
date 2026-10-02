import yaml
from pathlib import Path
from docgen.data_fetcher import DataFetcher
from docgen.entities import Project, create_workers_from_map
from docgen.generators import generate_act, generate_task, generate_statement
from docgen.settings_manager import SettingsKey
from docxtpl import DocxTemplate
from typing import Dict

def get_projects(settings) -> Dict:
    fetcher = DataFetcher(settings.get("api_token"), settings.get("worker_table_path"))
    return {p["name"]: p["id"] for p in fetcher.get_projects()}


def generate_acts(project: Project, settings):
    '''Генерация актов.'''
    out_dir = get_output_dir(settings)
    for w in project.workers:
        doc = DocxTemplate(settings.get("act_template_path"))
        generate_act(doc, project, w)
        doc.save(str(out_dir / f"act_{w.initials()}.docx"))

def generate_tasks(project: Project, settings):
    '''Генерация задания.'''
    out_dir = get_output_dir(settings)
    doc = DocxTemplate(settings.get("task_template_path"))
    generate_task(doc, project)
    doc.save(str(out_dir / f"task_{project.font.name_and_version()}.docx"))

def generate_statements(project: Project, settings):
    '''Генерация заверения.'''
    out_dir = get_output_dir(settings)
    doc = DocxTemplate(settings.get("statement_template_path"))
    generate_statement(doc, project)
    doc.save(str(out_dir / f"statement_{project.font.name_and_version()}.docx"))

def get_project_data(project_name: str, settings) -> Project:
    '''Получение данных и формирование проекта.'''
    fetcher = DataFetcher(settings.get("api_token"), settings.get("worker_table_path"))
    
    workers_mapping = fetcher.get_workers_mapping()
    workers_data = fetcher.get_workers_data()
    projects = fetcher.get_projects()
    
    proj = next((p for p in projects if p["name"] == project_name), None)
    
    if proj is None:
        raise ValueError(f"Проект '{project_name}' не найден")

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


def get_output_dir(settings) -> Path:
    out_dir = settings.get(SettingsKey.OUTPUT_DIR)
    if not out_dir:
        raise ValueError("Не задана папка для сохранения (output_dir)")
    return Path(out_dir)