import json
import sys
from pathlib import Path

class SettingsKey:
    API_TOKEN = "api_token"
    WORKER_TABLE_PATH = "worker_table_path"
    TASK_TEMPLATE_PATH = "task_template_path"
    STATEMENT_TEMPLATE_PATH = "statement_template_path"
    ACT_TEMPLATE_PATH = "act_template_path"
    OUTPUT_DIR = "output_dir"

    @classmethod
    def all_keys(cls):
        return [getattr(cls, attr) for attr in dir(cls) if not attr.startswith("_") and attr.isupper()]

class SettingsManager:

    def __init__(self, filename="settings.json"):
        self.filename = filename
        self._settings = {}
        self._file_path = self._get_default_path()
        self.load()

    def _get_default_path(self):
        if getattr(sys, 'frozen', False):
            base_dir = Path(sys.executable).parent
        else:
            base_dir = Path.cwd()
        return base_dir / self.filename

    def load(self):
        if self._file_path.exists():
            try:
                with open(self._file_path, 'r', encoding='utf-8') as f:
                    self._settings = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._settings = {}
        else:
            self._settings = {}

    def save(self):
        try:
            with open(self._file_path, 'w', encoding='utf-8') as f:
                json.dump(self._settings, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Ошибка сохранения настроек: {e}")

    
    def get(self, key, default=None):
        return self._settings.get(key, default)

    def set(self, key, value):
        self._settings[key] = value
        self.save()

    def has(self, key):
        return key in self._settings

    def remove(self, key):
        if key in self._settings:
            del self._settings[key]
            self.save()

    def update(self, settings_dict):
        changed = False
        for key, value in settings_dict.items():
            if self.get(key) != value:
                self._settings[key] = value
                changed = True
        if changed:
            self.save()