import requests

import pytest
import os
from docgen.data_fetcher import DataFetcher

def get_api_token():
    token = os.environ.get("API_TOKEN")
    if token is None:
        pytest.skip("API_TOKEN not set, skipping integration tests")
    return token

@pytest.fixture
def path():
    if os.path.exists("src/test/fixtures/workers.xlsx"):
        return "src/test/fixtures/workers.xlsx"
    return None

mapping = {
    "Имя в базе": "ФИО",
    "Степашка": "Иванов Иван Иванович",
    "Директор": "Фамилия Имя Отчество"
}

data = {
    "Иванов Иван Иванович": ["Департамент производство", "Графический дизайнер", "20.06.2002", 
                             "Паспорт гражданина РФ", "693-788", "Отделом внутренних дел Ленинского р-на г. Екатеринбурга", 
                             "15.11.2014", "577471", "6786", "г. Москва, наб. Обводного канала, д. 133, кв. 103",
                             "046123663373", "АО \"АЛЬФА-БАНК\" №1", "79921665959502890126", "898698725"]
}

def test_fetcher_get_projects(path):
    api_token = get_api_token()
    fetcher = DataFetcher(path=path, token=api_token)
    try:
        projects = fetcher.get_projects()
    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        pytest.fail(f"HTTP error {status} while fetching projects")
    except Exception as e:
        pytest.fail(f"Unexpected error: {type(e).__name__}")
    
    if not projects:
        pytest.fail("No projects fetched")

def test_fetcher_with_invalid_token(path):
    fetcher = DataFetcher(path=path, token="invalid_token")
    try:
        fetcher.get_projects()
        pytest.fail("Expected exception not raised")
    except Exception:
        pass
    
def test_fetcher_with_invalid_path():
    try:
        DataFetcher(path="invalid_path", token="invalid_token")
        pytest.fail("Expected exception not raised")
    except Exception:
        pass

def test_fetcher_mapping(path):
    fetcher = DataFetcher(path=path, token="")
    try:
        names = fetcher.get_workers_mapping()
        assert names is not None
        assert names == mapping
    except Exception as e:
        pytest.fail(f"Exception occurred: {e}")

def test_fetcher_workers_data(path):
    fetcher = DataFetcher(path=path, token="")
    try:
        workers_data = fetcher.get_workers_data()
        assert workers_data is not None
        assert workers_data["Иванов Иван Иванович"] == data["Иванов Иван Иванович"]
    except Exception as e:
        pytest.fail(f"Exception occurred: {e}")
