from unittest.mock import MagicMock
import pytest

from docgen.data_fetcher import DataFetcher


@pytest.fixture
def fake_session(mocker):
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
                "start_date": "2024-01-15",
                "end_date": "2024-03-20",
                "authors": ["Ivanov Ivan Ivanovich"],
            }
        else:
            raise AssertionError(f"Unexpected URL: {url}")
        return resp

    session.get.side_effect = fake_get
    return session


def make_workers_xlsx(path):
    from openpyxl import Workbook
    wb = Workbook()
    ws0 = wb.active
    ws0.title = "Workers"
    # row[2] — ФИО, остальное в 15 столбцов
    row = [None] * 15
    row[2] = "Ivanov Ivan Ivanovich"
    row[3] = "outsource_yes"
    ws0.append(row)

    ws1 = wb.create_sheet("Mapping")
    ws1.append(["Иванов Иван Иванович", "Ivanov Ivan", None, None])

    wb.save(path)


def test_get_projects_returns_mapping(tmp_path, fake_session):
    xlsx = tmp_path / "w.xlsx"
    make_workers_xlsx(xlsx)

    fetcher = DataFetcher("token", str(xlsx), session=fake_session)
    assert fetcher.get_projects() == [
        {"id": 42, "name": "Alpha"},
        {"id": 7, "name": "Beta"},
    ]


def test_get_project_info(tmp_path, fake_session):
    xlsx = tmp_path / "w.xlsx"
    make_workers_xlsx(xlsx)
    fetcher = DataFetcher("token", str(xlsx), session=fake_session)

    info = fetcher.get_project_info(42)
    assert info["authors"] == ["Ivanov Ivan Ivanovich"]


def test_get_workers_mapping(tmp_path, fake_session):
    xlsx = tmp_path / "w.xlsx"
    make_workers_xlsx(xlsx)
    fetcher = DataFetcher("token", str(xlsx), session=fake_session)

    assert fetcher.get_workers_mapping() == {"Иванов Иван Иванович": "Ivanov Ivan"}