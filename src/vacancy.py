import textwrap

class Vacancy:
    """Класс для работы с вакансиями."""

    def __init__(self, title, location, url, salary_from, salary_to, currency, description):
        """
        Инициализирует объект класса и устанавливает значения для атрибутов вакансии.
        Args:
            title (str): Название вакансии.
            location (str): Регион или локация вакансии.
            url (str): Ссылка на вакансию.
            salary_from (float): Зарплата от.
            salary_to (float): Зарплата до.
            currency (str): Валюта зарплаты.
            description (str): Требования и описание вакансии.
        """

        self.title = title
        self.location = location
        self.url = url
        self.salary_from = salary_from
        if self.salary_from == None:
            self.salary_from = 0
        self.salary_to = salary_to
        self.currency = currency
        if self.currency == 'rub':
            self.currency = 'RUR'
        self.description = description
        if self.description == None:
            self.description = ''

    def __repr__(self):
        """Возвращает строковое представление объекта вакансии."""

        description_lines = textwrap.wrap(self.description, width=100)  # Разбиваем строку на строки шириной 100 символов
        description = '\n'.join(description_lines)  # Объединяем строки с переносом строки
        return (
            f"\nВакансия: {self.title}\n"
            f"Регион: {self.location}\n"
            f"Ссылка на вакансию: {self.url}\n"
            f"Зарплата от {self.salary_from} {self.currency}\n"
            f"Описание вакансии:\n{description}\n"
        )

    def __eq__(self, other):
        """Проверяет, равны ли два объекта вакансии по зарплате."""

        return self.salary_from == other.salary

    def __lt__(self, other):
        """Сравнивает два объекта вакансии по зарплате."""

        if other.salary_from is None:
            return True
        if self.salary_from is None:
            return False
        return self.salary_from < other.salary_from