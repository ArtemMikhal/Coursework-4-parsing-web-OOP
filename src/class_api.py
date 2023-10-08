# Создать абстрактный класс для работы с API сайтов с вакансиями.
# Реализовать классы, наследующиеся от абстрактного класса,
# для работы с конкретными платформами.
# Классы должны уметь подключаться к API и получать вакансии.
from abc import ABC, abstractmethod
import requests
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
        """Реалиует подключение к API конкретной платформы."""
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
        """Реализует получение информации о вакансии с платформы"""
        response = self.connect() # Выполняем запрос методом self.connect(). Он возвращает response объект.
        if response: # Производим проверку на None/False. Если response не пуст, то запрос прошел успешно.
            return response.json() # десериализуем JSON ответ в python объекты командой json() и возвращаем их.
        else: # Если response = None, то запрос не удался.
            print("Запрос не удался, вакансии не получены") # выводим сооьщение что вакансии не были получены.


class SuperJobAPI(JobSitesAPI): # Класс для SuperJobAPI


    def connect(self):
        # Реализация подключения к API конкретной платформы
        pass


    def get_jobs(self):
        # Реализация получения вакансий с платформы
        pass






