from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Сутність Співробітники
class Employee(models.Model):
    employee_code = models.CharField(max_length=50, unique=True, verbose_name="Код співробітника")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    first_name = models.CharField(max_length=50, verbose_name="Ім’я")
    middle_name = models.CharField(max_length=50, verbose_name="По батькові")
    address = models.CharField(max_length=255, verbose_name="Адреса")
    phone = models.CharField(max_length=20, verbose_name="Телефон")  # Маска вводу задається через форму
    education = models.CharField(
        max_length=20,
        choices=[('спеціальна', 'Спеціальна'), ('середня', 'Середня'), ('вища', 'Вища')],
        verbose_name="Освіта"
    )
    department_code = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
        verbose_name="Код відділу"
    )
    position_code = models.ForeignKey(
        'Position',
        on_delete=models.CASCADE,
        verbose_name="Код посади"
    )

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


# Сутність Відділи
class Department(models.Model):
    department_code = models.CharField(max_length=50, unique=True, verbose_name="Код відділу")
    name = models.CharField(max_length=100, verbose_name="Назва відділу")
    phone = models.CharField(max_length=20, verbose_name="Телефон")  # Маска вводу задається через форму
    room_number = models.PositiveIntegerField(
        verbose_name="Номер кімнати",
        validators=[MinValueValidator(701), MaxValueValidator(710)]  # Виправлено імпорт валідаторів
    )

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.name


# Сутність Посади
class Position(models.Model):
    position_code = models.CharField(max_length=50, unique=True, verbose_name="Код посади")  # Замінили на CharField
    title = models.CharField(max_length=100, verbose_name="Посада")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Оклад")
    bonus_percent = models.PositiveIntegerField(verbose_name="Премія (%)")

    class Meta:
        db_table = 'positions'

    def __str__(self):
        return self.title


# Сутність Проекти
class Project(models.Model):
    project_number = models.CharField(max_length=50, unique=True, verbose_name="Номер проекту")
    name = models.CharField(max_length=100, verbose_name="Назва проекту")
    deadline = models.DateField(verbose_name="Термін виконання")
    budget = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Розмір фінансування")

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.name


# Сутність Виконання проектів
class ProjectExecution(models.Model):
    execution_code = models.CharField(max_length=50, unique=True, verbose_name="Код виконання")
    project_number = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="Номер проекту"
    )
    department_code = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name="Код відділу"
    )
    start_date = models.DateField(verbose_name="Дата початку")

    class Meta:
        db_table = 'project_executions'

    def __str__(self):
        return self.execution_code
