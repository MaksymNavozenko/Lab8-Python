# Використовуємо офіційний Python образ
FROM python:3.9-slim

# Встановлюємо робочу директорію
WORKDIR /myproject

# Копіюємо requirements.txt та інсталуємо необхідні пакети
COPY requirements.txt /myproject/
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо всі файли проекту в контейнер (зокрема manage.py)
COPY . /myproject/

# Відкриваємо порт для веб-сервера
EXPOSE 8000

# Стартуємо Django
CMD ["python", "myproject/manage.py", "runserver", "0.0.0.0:8000"]
