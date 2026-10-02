import pytest
import requests

from docgen.data_fetcher import DataFetcher


pytestmark = pytest.mark.integration


def test_get_projects_real(api_token, workers_xlsx):
    fetcher = DataFetcher(token=api_token, path=workers_xlsx)
    projects = fetcher.get_projects()
    assert projects, "API вернул пустой список проектов"
    assert all("id" in p and "name" in p for p in projects)


def test_get_project_info_real(api_token, workers_xlsx):
    fetcher = DataFetcher(token=api_token, path=workers_xlsx)
    first = fetcher.get_projects()[0]
    info = fetcher.get_project_info(first["id"])
    assert info["status"] == "ok"
    assert "authors" in info
    assert "start_date" in info and "end_date" in info


def test_invalid_token_real(workers_xlsx):
    fetcher = DataFetcher(token="invalid_token", path=workers_xlsx)
    with pytest.raises(requests.HTTPError):
        fetcher.get_projects()