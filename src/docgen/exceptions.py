
class DocgenError(Exception):
    """Базовая ошибка приложения. Что-то пошло не так, но это ожидаемо."""
    default_title = "Ошибка"
    default_message = "Произошла ошибка"


class ProjectError(DocgenError):
    """Ошибка валидации/сборки проекта (например, из UI)."""
    default_title = "Некорректные данные"


class ProjectNotFoundError(DocgenError):
    """Проект с указанным именем не найден в API."""
    default_title = "Проект не найден"
    default_message = "Проект с указанным именем не найден в системе."


class WorkerDataError(DocgenError):
    """Данные о работниках неполные или противоречивые."""
    default_title = "Неполные данные о работниках"
    default_message = (
        "В таблице нет нужного работника или не хватает данных.\n"
        "Добавьте информацию и обновите проект."
    )


class DataSourceError(DocgenError):
    """Не удалось получить данные из внешнего источника (сеть, файл)."""
    default_title = "Ошибка источника данных"
    default_message = "Не удалось получить данные. Проверьте подключение и настройки."
    