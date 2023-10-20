import requests
from abc import ABC, abstractmethod\

class JobSitesAPI(ABC):
    """Абстрактный класс для работы с вакансиями по API."""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_jobs(self):
        pass


class HeadHunterAPI(JobSitesAPI):
    """Класс для работы с вакансиями по API с hh.ru."""

    url = "https://api.hh.ru/vacancies"

    def __init__(self, keyword):
        """
        Инициализирует объект класса и устанавливает параметры для запроса к API HeadHunter.
        Args:
            keyword (str): Ключевое слово для поиска вакансий.
        Attributes:
            params (dict): Параметры запроса к API HeadHunter.
            headers (dict): Заголовки запроса к API HeadHunter.
        """

        self.params = {
            "per_page": 100,  # количество вакансий на странице.
            "page": None,  # номер страницы результатов.
            "text": keyword,  # строка поиска по названию вакансии.
        }
        self.headers = {
            "HH-User-Agent": "PyCharm Scraper"
        }  # заголовок запроса к API HeadHunter.

    def connect(self):
        """Реалиует подключение к API hh.ru."""

        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.ok:
            return response
        else:
            print("Запрос не выполнен")

        return response

    def get_jobs(self):
        """Реализует получение информации о вакансиях с hh.ru"""
        response = self.connect()
        if response:
            data = response.json()

            jobs_list = []

            for job in data["items"]:
                title = job.get("name")
                location = job["area"].get("name")
                url = job.get("alternate_url")
                salary_from = (
                    job["salary"].get("from") if job["salary"] is not None else None
                )
                salary_to = (
                    job["salary"].get("to") if job["salary"] is not None else None
                )
                currency = (
                    job["salary"].get("currency") if job["salary"] is not None else None
                )
                description = job.get("snippet", {}).get("requirement")

                job_dict = {
                    "title": title,
                    "location": location,
                    "url": url,
                    "salary_from": salary_from,
                    "salary_to": salary_to,
                    "currency": currency,
                    "description": description,
                }
                jobs_list.append(job_dict)

            return jobs_list
        else:
            print("Запрос не удался, вакансии не получены")


class SuperJobAPI(JobSitesAPI):
    """Класс для работы с вакансиями по API с SuperJob."""

    url = "https://api.superjob.ru/2.0/vacancies/"

    def __init__(self, keyword):
        """
            Инициализирует объект класса и устанавливает параметры для запроса к API SuperJob.
            Args:
                keyword (str): Ключевое слово для поиска вакансий.
            Attributes:
                params (dict): Параметры запроса к API SuperJob.
                headers (dict): Заголовки запроса к API SuperJob.
        """

        self.params = {"count": 100, "page": None, "keyword": keyword, "archive": False}
        self.headers = {
            "User-Agent": "PyCharm Scraper",  # Заголовок запроса к API SuperJob
            "X-Api-App-Id": "v3.r.137882423.3f16d7b38ae40fcdf737015f09b7f73acd57de42.b234710085d1ec74c3252957807ea272da9d4432",
        }

    def connect(self):
        """Реализует подключение к API SuperJob."""
        response = requests.get(self.url, headers=self.headers, params=self.params)
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
            for job in data["objects"]:
                title = job.get("profession")
                location = job["town"].get("title")
                url = job.get("link")
                salary_from = job.get("payment_from")
                salary_to = job.get("payment_to")
                currency = job.get("currency")
                description = job.get("candidat")

                job_dict = {
                    "title": title,
                    "location": location,
                    "url": url,
                    "salary_from": salary_from,
                    "salary_to": salary_to,
                    "currency": currency,
                    "description": description,
                }
                jobs_list.append(job_dict)

            return jobs_list
        else:
            print("Запрос не удался, вакансии не получены")
