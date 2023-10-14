"""Определить абстрактный класс, который обязывает
реализовать методы для добавления вакансий в файл,
получения данных из файла по указанным критериям и удаления
информации о вакансиях. Создать класс для сохранения информации
о вакансиях в JSON-файл. Дополнительно (по желанию) можно реализовать
классы для работы с другими форматами, например с CSV-, Excel- или TXT-файлом."""
import json
from abc import ABC, abstractmethod
class JobStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        """Абстрактный метод для добавления вакансии в хранилище"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        """
        Абстрактный метод для получения списка вакансий из хранилища,
        соответствующих указанным критериям.
        """


    @abstractmethod
    def  delete_vacancy(self, vacancy_id):
        """Абстрактный метод для удаления вакансии из хранилища"""
        pass


class JSONVacancyStorage(JobStorage):
    def __init__(self, file_path): # путь к  файлу в который передаем вакансии для хранения например save_job.json
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        with open(self.file_path, 'w', encoding='UTF-8') as json_file:
            json.dump(vacancy, json_file, ensure_ascii=False, indent=2)
            json_file.write('\n')



    def get_vacancies(self, criteria):
        result = []
        with open(self.file_path, 'r') as file:
            for line in file:
                vacancy = json.loads(line)
                if criteria in vacancy:
                    result.append(vacancy)
        return result

    def delete_vacancy(self, vacancy_id):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        with open(self.file_path, 'w') as file:
            for line in lines:
                vacancy = json.loads(line)
                if vacancy.get('id') != vacancy_id:
                    file.write(line)