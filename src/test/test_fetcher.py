from unittest.mock import MagicMock

import pytest
import requests

from docgen.data_fetcher import DataFetcher
from conftest import EXPECTED_MAPPING, EXPECTED_WORKERS_DATA


@pytest.fixture
def fake_session():
    """Мок requests.Session с эмуляцией двух эндпоинтов API."""
    session = MagicMock()

    def fake_get(url, params=None, verify=False):
        resp = MagicMock()
        resp.raise_for_status = MagicMock()
        if url.endswith("/projects"):
            resp.json.return_value = {
                "projects": [{"id": 42, "name": "Alpha"}, {"id": 7, "name": "Beta"}]
            }
        elif "/project/42/authors-summary" in url:
            resp.json.return_value = {
                "status": "ok",
                "project_id": 42,
                "start_date": "2024-01-15",
                "end_date": "2024-03-20",
                "authors": [
                    {"name": "Степашка", "position": "Дизайнер",
                     "is_outsource": False, "tasks": []},
                ],
            }
        else:
            raise AssertionError(f"Unexpected URL: {url}")
        return resp

    session.get.side_effect = fake_get
    return session


# ---------- проекты ----------

def test_get_projects_returns_list(workers_xlsx, fake_session):
    fetcher = DataFetcher(token="t", path=workers_xlsx, session=fake_session)
    assert fetcher.get_projects() == [
        {"id": 42, "name": "Alpha"},
        {"id": 7, "name": "Beta"},
    ]


def test_get_projects_passes_token_in_params(workers_xlsx, fake_session):
    fetcher = DataFetcher(token="SECRET", path=workers_xlsx, session=fake_session)
    fetcher.get_projects()

    _, kwargs = fake_session.get.call_args
    assert kwargs["params"]["token"] == "SECRET"


def test_get_projects_propagates_http_error(workers_xlsx):
    session = MagicMock()
    resp = MagicMock()
    resp.raise_for_status.side_effect = requests.HTTPError("500 Server Error")
    session.get.return_value = resp

    fetcher = DataFetcher(token="t", path=workers_xlsx, session=session)
    with pytest.raises(requests.HTTPError):
        fetcher.get_projects()


# ---------- информация о проекте ----------

def test_get_project_info(workers_xlsx, fake_session):
    fetcher = DataFetcher(token="t", path=workers_xlsx, session=fake_session)
    info = fetcher.get_project_info(42)
    assert info["status"] == "ok"
    assert info["authors"][0]["name"] == "Степашка"


def test_get_project_info_unknown_id(workers_xlsx, fake_session):
    fetcher = DataFetcher(token="t", path=workers_xlsx, session=fake_session)
    with pytest.raises(AssertionError, match="Unexpected URL"):
        fetcher.get_project_info(999)


# ---------- xlsx ----------

def test_get_workers_mapping(workers_xlsx, fake_session):
    fetcher = DataFetcher(token="t", path=workers_xlsx, session=fake_session)
    assert fetcher.get_workers_mapping() == EXPECTED_MAPPING


def test_get_workers_data(workers_xlsx, fake_session):
    fetcher = DataFetcher(token="t", path=workers_xlsx, session=fake_session)
    data = fetcher.get_workers_data()
    assert "Иванов Иван Иванович" in data
    assert data["Иванов Иван Иванович"] == EXPECTED_WORKERS_DATA["Иванов Иван Иванович"]


def test_get_workers_mapping_raises_on_missing_pair(tmp_path):
    from openpyxl import Workbook

    p = tmp_path / "bad.xlsx"
    wb = Workbook()
    ws0 = wb.active
    ws0.title = "Data"
    ws0.append([None] * 15)
    ws1 = wb.create_sheet("Map")
    ws1.append(["Степашка", None, None, None])
    wb.save(str(p))

    fetcher = DataFetcher(token="t", path=str(p))
    with pytest.raises(ValueError, match="Степашка"):
        fetcher.get_workers_mapping()


# ---------- ошибки создания ----------

def test_invalid_path_raises():
    with pytest.raises((FileNotFoundError, ValueError)):
        DataFetcher(token="t", path="/nope/does-not-exist.xlsx")


def test_none_path_raises_type_error():
    with pytest.raises(TypeError):
        DataFetcher(token="t", path=None)