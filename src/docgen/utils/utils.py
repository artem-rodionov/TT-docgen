from typing import List
from entities import Worker

RUSSIAN_MONTHS = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
}

def get_right_date(value: int) -> str:
    if int(value) / 10 < 1:
            return "0" + str(value)
    return str(value)

def find_max_full_name(workers: List[Worker]) -> int:
      return max([len(w.full_name()) for w in workers])

def split_into_columns(items, num_columns=3):
    total = len(items)
    part_size = (total + num_columns - 1) // num_columns
    cols = []
    for i in range(num_columns):
        start = i * part_size
        end = start + part_size
        cols.append(items[start:end])
    return cols
# def get_font_instances(file_or_path: Any) -> List[str]:
#     font = glyphsLib.load(file_or_path)
#     return [instance.familyName + ' ' +
#             instance.name for instance in font.instances]