import requests
from pathlib import Path
from docgen.data_fetcher import DataFetcher
from docgen.entities import Project, create_workers_from_map
from docgen.generators import generate_act, generate_task, generate_statement
from docgen.settings_manager import SettingsKey
from docgen.exceptions import (
    ProjectNotFoundError,
    DataSourceError,
    WorkerDataError,
    DocgenError
)
from docxtpl import DocxTemplate
from typing import Dict

def _make_fetcher(settings, factory=DataFetcher) -> DataFetcher:
    try:
        return factory(settings.get(SettingsKey.API_TOKEN),
                       settings.get(SettingsKey.WORKER_TABLE_PATH)
                       )
    except (OSError, ValueError, TypeError) as e:
        raise WorkerDataError(f"Не удалось прочитать таблицу работников: {e}") from e

def get_projects(settings) -> Dict:
    fetcher = _make_fetcher(settings)
    projects = _fetch(fetcher.get_projects)
    return {p["name"]: p["id"] for p in projects}

def _fetch(fn, *args, **kwargs):
    """Обёртка: любые сетевые ошибки превращаем в DataSourceError."""
    try:
        return fn(*args, **kwargs)
    except requests.HTTPError as e:
        status = e.response.status_code if e.response is not None else "?"
        raise DataSourceError(f"Сервис вернул ошибку {status}") from e
    except requests.RequestException as e:
        raise DataSourceError(f"Не удалось подключиться к сервису: {e}") from e

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

def get_project_data(project_name: str, settings,
                     fetcher_factory=DataFetcher) -> Project:
    """Получение данных и формирование проекта.

    Бросает:
      - WorkerDataError       — проблемы с xlsx или отсутствующим работником;
      - ProjectNotFoundError  — проекта нет в API;
      - DataSourceError       — сеть/сервер недоступны.
    """
    fetcher = _make_fetcher(settings, fetcher_factory)

    try:
        workers_mapping = fetcher.get_workers_mapping()
        workers_data = fetcher.get_workers_data()
    except ValueError as e:
        raise WorkerDataError(str(e)) from e

    projects = _fetch(fetcher.get_projects)

    proj = next((p for p in projects if p["name"] == project_name), None)
    if proj is None:
        raise ProjectNotFoundError(f"Проект '{project_name}' не найден")

    project_info = _fetch(fetcher.get_project_info, proj["id"])

    try:
        workers = create_workers_from_map(
            project_info["authors"], workers_data, workers_mapping
        )
    except KeyError as e:
        raise WorkerDataError(
            f"В таблице нет работника: {e}"
        ) from e
    except ValueError as e:
        raise WorkerDataError(str(e)) from e

    return Project(
        work_name=proj["name"],
        final_name=None,
        start=project_info["start_date"],
        end=project_info["end_date"],
        style=None,
        workers=workers,
        font=None,
        head=workers[0],
    )


def get_output_dir(settings) -> Path:
    out_dir = settings.get(SettingsKey.OUTPUT_DIR)
    if not out_dir:
        raise DocgenError("Не задана папка для сохранения (output_dir)")
    return Path(out_dir)