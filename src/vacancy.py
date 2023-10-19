# Создать класс для работы с вакансиями.
# В этом классе самостоятельно определить атрибуты,
# такие как название вакансии, ссылка на вакансию,
# зарплата, краткое описание или требования и т. п. (не менее четырех).
# Класс должен поддерживать методы сравнения вакансий
# между собой по зарплате и валидировать данные, которыми инициализируются его атрибуты.

class Vacancy:
    def __init__(self, title, location, url, salary_from, salary_to, currency, description):
        self.title = title # Название вакансии
        self.location = location # Регион, локация
        self.url = url # Ссылка
        self.salary_from = salary_from # Зарплата от
        #if self.salary_from == None or 0:
            #self.salary_from = salary_to
        self.salary_to = salary_to # Зарплата до
        #if self.salary_to == None or 0:
            #self.salary_to = salary_from
        self.currency = currency # Валюта
        self.description = description # Требования,описание вакансии



    def __repr__(self):
        return f" Вакансия: {self.title}" \
               f" Регион: {self.location}" \
               f" Ссыка на вакансию:  {self.url}" \
               f" Зарплата от {self.salary_from}"


    def __eq__(self, other):
        return self.salary_from == other.salary

    def __lt__(self, other):
        if other.salary_from is None or 0:
            return True
        if self.salary_from is None or 0:
            return False
        return self.salary_from < other.salary_from

    #добавить метод repl или str (чтобы выводилась инфа хз так сказал наставник)



    def validate(self):
        # Реализуйте логику валидации данных вакансии
        if not isinstance(self.title, str):
            raise ValueError("Название вакансии должно быть строкой")
        if not isinstance(self.location, str):
            raise ValueError("Регион должен быть строкой")
        if not isinstance(self.link, str):
            raise ValueError("Ссылка должна быть строкой")
        if not isinstance(self.salary_from, (int, float)):
            raise ValueError("Зарплата от должна быть числом")
        if not isinstance(self.salary_to, (int, float)):
            raise ValueError("Зарплата до должна быть числом")
        if not isinstance(self.currency, str):
            raise ValueError("Валюта должна быть строкой")
        if not isinstance(self.description, str):
            raise ValueError("Описание должно быть строкой")


