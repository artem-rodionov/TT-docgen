import os
from pathlib import Path

import pytest
from openpyxl import Workbook


EXPECTED_MAPPING = {
    "Имя в базе": "ФИО",
    "Степашка": "Иванов Иван Иванович",
    "Директор": "Фамилия Имя Отчество",
}

EXPECTED_WORKERS_DATA = {
    "Иванов Иван Иванович": [
        "Департамент производство", "Графический дизайнер", "20.06.2002",
        "Паспорт гражданина РФ", "693-788",
        "Отделом внутренних дел Ленинского р-на г. Екатеринбурга",
        "15.11.2014", "577471", "6786",
        "г. Москва, наб. Обводного канала, д. 133, кв. 103",
        "046123663373", 'АО "АЛЬФА-БАНК" №1',
        "79921665959502890126", "898698725",
    ]
}


def build_workers_xlsx(path: Path) -> Path:
    """xlsx со структурой боевого файла:
       лист 0 — данные работников (15 колонок),
       лист 1 — маппинг (кличка → ФИО).
    """
    wb = Workbook()

    ws_data = wb.active
    ws_data.title = "Data"
    row = [
        "Департамент производство", "Графический дизайнер",
        "Иванов Иван Иванович", "20.06.2002",
        "Паспорт гражданина РФ", "693-788",
        "Отделом внутренних дел Ленинского р-на г. Екатеринбурга",
        "15.11.2014", "577471", "6786",
        "г. Москва, наб. Обводного канала, д. 133, кв. 103",
        "046123663373", 'АО "АЛЬФА-БАНК" №1',
        "79921665959502890126", "898698725",
    ]
    ws_data.append(row)

    ws_map = wb.create_sheet("Map")
    for k, v in EXPECTED_MAPPING.items():
        ws_map.append([k, v, None, None])

    wb.save(str(path))
    return path


@pytest.fixture
def workers_xlsx(tmp_path) -> str:
    """Изолированный xlsx, генерируется на каждый тест."""
    return str(build_workers_xlsx(tmp_path / "workers.xlsx"))

@pytest.fixture(scope="session")
def api_token():
    token = os.environ.get("API_TOKEN")
    if not token:
        pytest.skip("API_TOKEN не задан — интеграционные тесты пропущены")
    return token