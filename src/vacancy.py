# Создать класс для работы с вакансиями.
# В этом классе самостоятельно определить атрибуты,
# такие как название вакансии, ссылка на вакансию,
# зарплата, краткое описание или требования и т. п. (не менее четырех).
# Класс должен поддерживать методы сравнения вакансий
# между собой по зарплате и валидировать данные, которыми инициализируются его атрибуты.

class Vacancy:
    def __init__(self, title, location, link, salary, description):
        self.title = title # Название вакансии
        self.location = location # Регион, локация
        self.link = link # Ссылка
        self.salary = salary # Зарплата
        self.description = description # Требования,описание вакансии

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def validate(self):
        # Реализуйте логику валидации данных вакансии
        pass


