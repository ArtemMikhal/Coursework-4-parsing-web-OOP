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
        with open(self.file_path, 'r', encoding='utf-8') as file:

            vacancies = json.load(file)
            for vacancy in vacancies:
                for value in vacancy.values():
                    if criteria in str(value):
                        result.append(vacancy)
        with open(self.file_path, 'w', encoding='UTF-8') as json_file:
            json.dump(result, json_file, ensure_ascii=False, indent=2)
            json_file.write('\n')

        return result

    def delete_vacancy(self, criteria):
        with open(self.filename) as f:
            data = json.load(f)

        for vacancy in data:
            # Сравниваем непосредственно в цикле
            if vacancy != criteria:
                data.remove(vacancy)

        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_vacancy(self):
        #Загр json файл  и возвр список словарей
        with open(self.file_path, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
            return vacancies


    def len_vacancy(self):
        """Считает количество вакансий"""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
        count = len(vacancies)
        return count