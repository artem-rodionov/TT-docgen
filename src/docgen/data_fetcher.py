import requests
from openpyxl import load_workbook

class DataFetcher:
    def __init__(self, token: str, path: str,
                 base_url: str = "https://uchet.type-tech.ru/api",
                 session: requests.Session | None = None,
                 verify: bool = False) -> None:
        self.token = token
        self.base_url = base_url.rstrip("/")
        self.table = load_workbook(path, data_only=True)
        self.session = session or requests.Session()
        self.verify = verify

    def _get(self, endpoint: str) -> dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params={"token": self.token}, verify=self.verify)
        response.raise_for_status()
        return response.json()

    def get_projects(self):
        '''Получение списка всех проектов.'''
        return self._get("projects")["projects"]
    
    def get_project_info(self, project_id):
        '''Получение информации о проекте.'''
        return self._get(f"project/{project_id}/authors-summary")
    
    def get_workers_mapping(self):
        '''Получение соответствия ФИО и имен из БД.'''
        sheet = self.table.worksheets[1]
        names = {}
        for row in sheet.iter_rows(values_only=True):
            i = 0
            while i < len(row):
                cell = row[i]
                if cell is None or str(cell).strip() == "":
                    i += 1
                    continue
                
                col = str(cell).strip()
                next_cell = row[i + 1] if i + 1 < len(row) else None
                if next_cell is None or str(next_cell).strip() == "":
                    raise ValueError(f"Для '{col}' не указано соответствие")
                
                names[col] = str(next_cell).strip()
                i += 2
        return names

    def get_workers_data(self):
        '''Получение данных о работниках.'''
        sheet = self.table.worksheets[0]
        workers = {}
        for row in sheet.iter_rows(values_only=True):
            if row[2] is None:
                continue
            other_cols = [row[i] for i in range(15) if i != 2]

            workers[str(row[2]).strip()] = other_cols

        return workers