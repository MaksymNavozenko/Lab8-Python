import random
from faker import Faker
from django.core.management.base import BaseCommand
from myapp.models import Department, Employee, Position, Project, ProjectExecution  # Замініть 'myapp' на назву вашого додатка

fake = Faker("uk_UA")

class Command(BaseCommand):
    help = "Populate database with fake data"

    def handle(self, *args, **kwargs):
        # Генерація даних для Department
        departments = ["HR", "IT", "Finance", "Logistics", "Production"]
        for department_name in departments:
            Department.objects.create(
                department_code=f"DEP-{random.randint(100, 999)}",  # Генерація унікального коду
                name=department_name,
                phone=f"+38067{random.randint(1000000, 9999999)}",
                room_number=random.randint(701, 710)  # Відповідає валідації
            )

        # Генерація даних для Position
        positions = [
            {"position_code": f"POS-{random.randint(100, 999)}", "title": "Менеджер", "salary": 15000, "bonus_percent": 10},
            {"position_code": f"POS-{random.randint(100, 999)}", "title": "Інженер", "salary": 20000, "bonus_percent": 15},
            {"position_code": f"POS-{random.randint(100, 999)}", "title": "Оператор", "salary": 12000, "bonus_percent": 5},
        ]
        for position in positions:
            Position.objects.create(
                position_code=position["position_code"],
                title=position["title"],
                salary=position["salary"],
                bonus_percent=position["bonus_percent"]
            )

        # Генерація даних для Employee
        department_objs = Department.objects.all()
        position_objs = Position.objects.all()
        for _ in range(15):  # 15 працівників
            Employee.objects.create(
                employee_code=f"EMP-{random.randint(1000, 9999)}",  # Генерація унікального коду
                last_name=fake.last_name(),
                first_name=fake.first_name(),
                middle_name=fake.middle_name(),
                address=fake.address(),
                phone=f"+38067{random.randint(1000000, 9999999)}",
                education=random.choice(['спеціальна', 'середня', 'вища']),
                department_code=random.choice(department_objs),
                position_code=random.choice(position_objs)
            )

        # Генерація даних для Project
        for _ in range(8):  # 8 проектів
            Project.objects.create(
                project_number=f"PR-{random.randint(1000, 9999)}",
                name=fake.bs(),
                deadline=fake.date_between(start_date="today", end_date="+90d"),
                budget=random.uniform(50000, 200000)
            )

        # Генерація даних для ProjectExecution
        project_objs = Project.objects.all()
        for project in project_objs:
            ProjectExecution.objects.create(
                execution_code=f"EX-{random.randint(1000, 9999)}",  # Генерація унікального коду
                project_number=project,
                department_code=random.choice(department_objs),
                start_date=fake.date_between(start_date="today", end_date="+30d")
            )

        self.stdout.write(self.style.SUCCESS("Database populated successfully!"))
