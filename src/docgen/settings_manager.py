import json
import sys
from pathlib import Path

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