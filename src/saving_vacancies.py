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
    def add_job(self, job):
        """Абстрактный метод для добавления вакансии в хранилище"""
        pass

    @abstractmethod
    def get_jobs(self, criteria):
        """
        Абстрактный метод для получения списка вакансий из хранилища,
        соответствующих указанным критериям.
        """


    @abstractmethod
    def delete_job(self, job):
        """Абстрактный метод для удаления вакансии из хранилища"""
        pass


class JSONJobStorage(JobStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def add_job(self, job):
        """Метод для добавления вакансии в JSON-файл хранилища."""
        job_data = {
            'title': job.title,
            'location': job.location,
            'link': job.link,
            'salary': job.salary,
            'description': job.description
        }
        with open(self.file_path, 'a') as file:
            json.dump(job_data, file)
            file.write('\n')

    def get_jobs(self, criteria):
        """Метод для получения списка вакансий из JSON-файла хранилища,
        соответствующих указанным критериям.
        """
        jobs = []
        with open(self.file_path, 'r') as file:
            for line in file:
                job_data = json.loads(line)
                job = Job(
                    job_data['title'],
                    job_data['location'],
                    job_data['link'],
                    job_data['salary'],
                    job_data['description']
                )
                if self._matches_criteria(job, criteria):
                    jobs.append(job)
        return jobs

    def delete_job(self, job):
        """Метод для удаления вакансии из JSON-файла хранилища."""
        lines = []
        with open(self.file_path, 'r') as file:
            for line in file:
                job_data = json.loads(line)
                existing_job = Job(
                    job_data['title'],
                    job_data['link'],
                    job_data['salary'],
                    job_data['description']
                )
                if existing_job != job:
                    lines.append(line)
        with open(self.file_path, 'w') as file:
            file.writelines(lines)

    def _matches_criteria(self, job, criteria):
        """Метод для реализации логики сравнения данных вакансии с критериями."""
        pass