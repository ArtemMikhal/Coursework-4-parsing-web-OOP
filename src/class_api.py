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
        """Реализует получение информации о вакансиях с hh.ru"""
        response = self.connect()
        if response:
            data = response.json()
            print(data)

            jobs_list = []
            for job in data['items']:
                title = job.get('name')
                location = job['area'].get('name')
                url = job.get('alternate_url')
                salary_from = job['salary'].get('from') if job['salary'] is not None else None
                salary_to = job['salary'].get('to') if job['salary'] is not None else None
                currency = job['salary'].get('currency') if job['salary'] is not None else None
                description = job.get('snippet', {}).get('requirement')

                job_dict = {
                    'title': title,
                    'location': location,
                    'url': url,
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                    'currency': currency,
                    'description': description
                }
                jobs_list.append(job_dict)
            print(jobs_list)
            final_dict = {
                'HH': jobs_list}
            return final_dict # возвращаем список словарей с нужными параметрами вакансий
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
            data = response.json()


            jobs_list = []
            for job in data['objects']:
                title = job.get('profession')
                location = job['town'].get('title')
                url = job.get('link')
                salary_from = job.get('payment_from')
                salary_to = job.get('payment_to')
                currency = job.get('currency')
                description = job.get('candidat')

                job_dict = {
                    'title': title,
                    'location': location,
                    'url': url,
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                    'currency': currency,
                    'description': description
                }
                jobs_list.append(job_dict)
            print(jobs_list)
            final_dict = {
                'SJ': jobs_list}
            print(final_dict)
            return final_dict  # возвращаем список словарей с нужными параметрами вакансий

        else:
            print("Запрос не удался, вакансии не получены")






