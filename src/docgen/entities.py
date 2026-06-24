import glyphsLib
import enum
from typing import List, Dict
from datetime import date, datetime

class WorkType(enum.Enum):
    Create = ("Создать", "созданием", "созданию")
    Update = ("Обновить", "обновлением", "обновлению")

    def __init__(self, infinitive, instrumental, dative):
        self.first = infinitive
        self.second = instrumental
        self.third = dative

class Font:
    '''Класс шрифта'''
    def __init__(self, file_or_path):
        font = glyphsLib.load(file_or_path)
        self.font_name = font.familyName
        self.font_instances = [instance.familyName + ' ' +
            instance.name for instance in font.instances]
        self.font_instances.sort()
        self.version = "Версия " + str(font.versionMajor) + '.' + str(font.versionMinor)

    def name_and_version(self) -> str:
        return self.font_name + ' ' + self.version

class Passport:
    def __init__(self, data):
        self.type = data[1]
        self.code = data[2]
        self.issueAuthority = data[3]

        format_str = "%d.%m.%Y"
        self.date = datetime.strptime(data[4], format_str)
        self.number = data[5]
        self.series = data[6]
        self.birth_date = data[0]

    def __str__(self) -> str:
        return f"{self.series} {self.number}"

class Worker:
    '''Класс работника'''
    def __init__(self, last_name: str, first_name: str, patronymic: str, outsource: bool, position: str, tasks: List[Dict], passport: Passport, inn: str) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.outsource = outsource
        self.position = position
        self.is_head = False
        self.tasks = tasks
        self.passport = passport
        self.inn = inn

    def full_name(self, InTable: bool = False) -> str:
        """Return the full name in the format: last name, first name, patronymic."""
        full_name = f"{self.last_name} {self.first_name} {self.patronymic}".strip()
        if InTable and self.is_head:
            return full_name + " - Руководитель проекта"
        return f"{self.last_name} {self.first_name} {self.patronymic}".strip()
    
    def get_position(self) -> str:
        if self.is_head:
            return self.position + " (руководитель проекта)"
        return self.position

    def initials(self) -> str:
        return f"{self.last_name} {self.first_name[0]}. {self.patronymic[0]}. ".strip()
    
    def roles(self) -> str:
        return ", ".join(task["name"] for task in self.tasks)

    @staticmethod
    def get_outsource_table(workers: List) -> List:
        """Return the table of outsource workers."""
        workers = [worker for worker in workers if worker.outsource]
        return workers
    
    @staticmethod
    def get_insource_table(workers: List) -> List:
        """Return the table of outsource workers."""
        workers = [worker for worker in workers if not worker.outsource]
        return workers


class Project:
    '''Класс проекта'''
    def __init__(self, work_name: str, final_name: str, start: str, end: str, style: str, workers: List[Worker], font: Font, head: Worker, type: WorkType = WorkType.Create):
        self.work_name = work_name
        self.final_name = final_name
        self.start_date = date.fromisoformat(start)
        self.end_date = date.fromisoformat(end)
        self.duration = count_duration(self.start_date, self.end_date)
        self.style = style
        self.workers = workers
        self.head = head
        self.font = font
        self.current_date = date.today()
        self.type = type

def count_duration(start: date, end: date) -> int:
    return (end.year - start.year) * 12 + end.month - start.month - (start.day < end.day)

def create_worker(worker_dict: Dict, data, mapping) -> Worker:
    name_in_base = worker_dict["name"]
    real_name = mapping[name_in_base]
    worker_data = data[real_name]
    passport = Passport(worker_data[2:9])
    full_name = real_name.split(" ")
    last_name = full_name[0]
    first_name = full_name[1]
    patronymic = full_name[2]
    position = worker_data[1]
    inn = worker_data[9]
    outsource = worker_dict["is_outsource"]
    tasks = worker_dict["tasks"]
    return Worker(
        last_name=last_name,
        first_name=first_name,
        patronymic=patronymic,
        outsource=outsource,
        position=position,
        tasks=tasks,
        passport=passport,
        inn=inn
    )

def create_workers_from_map(list_from_db: List, data, mapping_name) -> List[Worker]:
    workers = []
    
    for w in list_from_db:
        workers.append(create_worker(w, data, mapping_name))
    return workers

font_styles = [
    "Геометрический гротеск",
    "Модульный геометрический гротеск",
    "Скругленный геометрический гротеск",
    "Гуманистический гротеск",
    "Октогональный гротеск",
    "Текстовый гротеск",
    "Неогротеск",
    "Текстовый гротеск",
    "Моноширинный гротеск",
    "Акцидентный моноширинный гротеск",
    "Униширинный гротеск",
    "Гротеск куфи",
    "Гротеск насх",
    "Текстовая антиква",
    "Акцидентная антиква",
    "Акцидентная моноширинная антиква",
    "Новостильная антиква",
    "Переходная антиква",
    "Старостильная антиква",
    "Моноширинная антиква",
    "Брусковая антиква",
    "Ленточная антиква",
    "Комплект разностильный шрифтов",
    "Комплект акцидентных шрифтов",
    "Рукописный шрифт",
    "Рукописный акцидентный шрифт",
    "Акцидентный шрифт",
    "Акцидентная гарнитура",
    "Комплект рукописных шрифтов"
]