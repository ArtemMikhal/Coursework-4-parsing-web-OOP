# Создать абстрактный класс для работы с API сайтов с вакансиями.
# Реализовать классы, наследующиеся от абстрактного класса,
# для работы с конкретными платформами.
# Классы должны уметь подключаться к API и получать вакансии.
from src.vacancy import Vacancy
from abc import ABC, abstractmethod
import requests
import json
class JobSitesAPI(ABC):
    """Абстрактный класс для работы с вакансиями по API."""
    @abstractmethod # абстрактный метод connect
    def connect(self):
        pass


    @abstractmethod
    def get_jobs(self): # абстрактный метод get_jobs
        pass


class HeadHunterAPI(JobSitesAPI): # Класс для HeadHunterAPI
    url = 'https://api.hh.ru/vacancies' # ссылка на api вакансий hh.ru
    def __init__(self, keyword): # инициализация класса, указываем параметр keyword(вакансия вводится пользователем)
        self.params = {  # параметры для запроса
            "per_page": 30, # количество вакансий на странице. По умолчанию 30.
            "page": None, # номер страницы результатов. По умолчанию 1.
            "text": keyword, # строка поиска по названию вакансии. Например, "python"
        }
        self.headers = {"HH-User-Agent": "PyCharm Scraper"} # Заголовок запроса к API HeadHunter.


    def connect(self):
        """Реалиует подключение к API hh.ru."""
        response = requests.get(   # Осуществляем запрос к API платформы
            self.url,
            headers=self.headers,
            params=self.params
        )
        if response.ok:  # если запрос проходит
            return response # проверяем статус ответа Если True (запрос прошёл успешно), возвращаем response
        else:
            print("Запрос не выполнен") # Если False (запрос не прошёл) -выводим сообщение об ошибке

        return response # Но всё равно возвращаем response


    def get_jobs(self):
        """Реализует получение информации о вакансии с hh.ru"""
        response = self.connect()
        if response:
            data = response.json()
            print(data)
            # Обработка данных вакансий
            # Например, добавляем вакансии в JSON-хранилище
            for job in data['items']:
                title = job.get('name')
                location = job['area'].get('name')
                url = job.get('alternate_url')
                salary = job.get('salary')
                description = job.get('snippet', {}).get('requirement') # требования
                #self.storage.add_job(Vacancy(title, location, link, salary, description))

            # Преобразование данных в JSON и сохранение в файл
            json_data = json.dumps(data)
            print(json_data)
            with open('vacancies.json', 'w') as file:
                file.write(json_data)
        else:
            print("Запрос не удался, вакансии не получены")


class SuperJobAPI(JobSitesAPI): # Класс для SuperJobAPI
    url = 'https://api.superjob.ru/2.0/vacancies/' # ссылка на api вакансий SJ.ru

    def __init__(self, keyword):
        self.params = {
            "count": 30,
            "page": None,
            "keyword": keyword,
            "archive": False

        }
        self.headers = {
            "User-Agent": "PyCharm Scraper",  # Заголовок запроса к API SuperJob
            "X-Api-App-Id": "v3.r.137882423.3f16d7b38ae40fcdf737015f09b7f73acd57de42.b234710085d1ec74c3252957807ea272da9d4432" # Secret key
        }


    def connect(self):
        """Реализует подключение к API SuperJob."""
        response = requests.get(
            self.url,
            headers=self.headers,
            params=self.params
        )
        if response.ok:
            return response
        else:
            print("Запрос не выполнен")
        return response


    def get_jobs(self):
        """Реализует получение информации о вакансиях с платформы SuperJob."""
        response = self.connect()
        if response:
            return response.json()
        else:
            print("Запрос не удался, вакансии не получены")






