from datetime import date
from docxtpl import DocxTemplate
from typing import List, Dict, Any

from utils.utils import RUSSIAN_MONTHS, get_right_date, split_into_columns
from entities import Worker, Project



def generate_act(doc: DocxTemplate,project: Project, worker: Worker):
        start_month = RUSSIAN_MONTHS[project.start_date.month]
        current_date = date.today()
        current_month = RUSSIAN_MONTHS[current_date.month]
        passport_month = RUSSIAN_MONTHS[worker.passport.date.month]
        # end_month = RUSSIAN_MONTHS[project.end_date.month]
        if worker.outsource:
             money = "0"
        else:
             money = "1000"
    
        context = {
        'current_day': get_right_date(current_date.day),
        'current_month': current_month,
        'current_year': str(current_date.year),
        'font_creation_year': None,
        'author': worker,
        'font_typeface': project.font.name_and_version(),
        'passport_month': passport_month,
        'start_day': get_right_date(project.start_date.day),
        'start_month': start_month,
        'start_year': str(project.start_date.year),
        'money': money,
        }

        doc.render(context)

def generate_task(doc: DocxTemplate, project: Project):
    start_month = RUSSIAN_MONTHS[project.start_date.month]

    outsource = Worker.get_outsource_table(project.workers)
    insource = Worker.get_insource_table(project.workers)

    col1, col2, col3 = split_into_columns(project.font.font_instances)
    
    context = {
        'current_day': get_right_date(project.start_date.day),
        'current_month_str': start_month,
        'current_month': get_right_date(project.start_date.month),
        'current_year': str(project.start_date.year),
        'employees': insource,
        'non_employees': outsource,
        'font_typeface': project.font.name_and_version(),
        'project_manager': project.head,
        'start_day': get_right_date(project.start_date.day),
        'start_month': start_month,
        'start_year': str(project.start_date.year),
        'timeframe_months': project.duration,
        'typeface_style': project.style,
        'font_instances_count': len(project.font.font_instances),
        'font_instances': project.font.font_instances,
        'col1': col1,
        'col2': col2,
        'col3': col3,
        'workers': project.workers
    }

    doc.render(context)

def generate_statement(doc: DocxTemplate, project: Project):
    current_date = date.today()
    curr_month = RUSSIAN_MONTHS[current_date.month]
    start_month = RUSSIAN_MONTHS[project.start_date.month]
    end_month = RUSSIAN_MONTHS[project.end_date.month]
    
    context = {
        'current_day': get_right_date(current_date.day),
        'current_month': curr_month,
        'current_year': str(current_date.year),
        'font_creation_year': str(project.end_date.year),
        'font_typeface': project.font.name_and_version(),
        'project_manager': project.head,
        'start_day': get_right_date(project.start_date.day),
        'start_month': start_month,
        'start_year': str(project.start_date.year),
        'end_day': get_right_date(project.end_date.day),
        'end_month': end_month,
        'end_year': str(project.end_date.year),
        'workers': project.workers
    }

    doc.render(context)