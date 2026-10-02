import logging
from datetime import date
from typing import Callable

from docgen.core import generate_acts, generate_statements, generate_tasks
from docgen.entities import Font, Project, WorkType
from docgen.exceptions import ProjectError, DataSourceError

def build_project_from_ui_state(
    project: Project,
    *,
    start_date: date,
    end_date: date,
    current_date: date,
    style: str,
    font_path: str,
    head_index: int,
    work_type: WorkType,
    font_factory: Callable[[str], Font] = Font,
) -> Project:
    """Мутирует project согласно состоянию UI. Возвращает тот же объект."""
    if not font_path:
        raise ProjectError("Не выбран файл шрифта")
    if not style:
        raise ProjectError("Не выбран стиль")
    if not project.workers:
        raise ProjectError("У проекта нет работников")
    if not 0 <= head_index < len(project.workers):
        raise ProjectError(f"Некорректный индекс ответственного: {head_index}")

    project.start_date = start_date
    project.end_date = end_date
    project.current_date = current_date

    if project.head:
        project.head.is_head = False

    project.type = work_type
    project.style = style
    project.font = font_factory(font_path)

    project.head = project.workers[head_index]
    project.head.is_head = True

    project.workers.sort(key=lambda w: (not w.is_head, w.full_name()))
    return project


def generate_documents(
    project: Project,
    settings,
    *,
    do_task: bool,
    do_statement: bool,
    do_act: bool,
    progress_cb: Callable[[int], None] | None = None,
) -> None:
    """Запускает выбранные генераторы, дёргая progress_cb на каждом шаге."""

    def report(v: int) -> None:
        if progress_cb is not None:
            progress_cb(v)

    report(0)
    if do_task:
        logging.debug("Генерация задания...")
        generate_tasks(project, settings)
    report(33)

    if do_statement:
        logging.debug("Генерация заверения...")
        generate_statements(project, settings)
    report(66)

    if do_act:
        logging.debug("Генерация актов...")
        generate_acts(project, settings)
    report(100)


def fetch_projects_with_retry(
    settings,
    *,
    interval: float = 2.0,
    timeout: float = 10.0,
    fetch: Callable | None = None,
    sleep: Callable[[float], None] | None = None,
    clock: Callable[[], float] | None = None,
):
    """Возвращает dict проектов или бросает последнее исключение по таймауту."""
    from docgen.core import get_projects as default_fetch
    import time as _time

    fetch = fetch or default_fetch
    sleep = sleep or _time.sleep
    clock = clock or _time.time

    start = clock()
    last_error = None
    while clock() - start < timeout:
        try:
            projects = fetch(settings)
            if projects is not None:
                return projects
        except Exception as e:
            last_error = e
            logging.debug("Попытка получить проекты не удалась: %s", e)

        remaining = timeout - (clock() - start)
        if remaining <= 0:
            break
        sleep(min(interval, remaining))

    if last_error is not None:
        raise last_error
    raise DataSourceError(f"Сервис не отвечает: не удалось получить проекты за {timeout} секунд")