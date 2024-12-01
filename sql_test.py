import psycopg2
from prettytable import PrettyTable

# Підключення до бази даних
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="company_db",
        user="example_user",
        password="example_password"
    )

def execute_queries():
    connection = get_db_connection()
    cursor = connection.cursor()

    # 1. Відобразити всіх робітників, які мають оклад більший за 2000 грн. Відсортувати прізвища за алфавітом.
    cursor.execute(
        """
        SELECT e.last_name, e.first_name, p.salary
        FROM employees e
        JOIN positions p ON e.position_code_id = p.id;
        """
    )
    table = PrettyTable(["Прізвище", "Ім'я", "Оклад"])
    for row in cursor.fetchall():
        table.add_row(row)
    print("Робітники з окладом більшим за 2000 грн (сортування за прізвищем):\n", table)

    # 2. Порахувати середню зарплатню в кожному відділі
    cursor.execute(
        """
        SELECT d.name AS department_name, AVG(p.salary) AS avg_salary
        FROM employees e
        JOIN departments d ON e.department_code_id = d.id
        JOIN positions p ON e.position_code_id = p.id
        GROUP BY d.name;
        """
    )
    table = PrettyTable(["Відділ", "Середня зарплата"])
    for row in cursor.fetchall():
        table.add_row(row)
    print("\nСередня зарплата в кожному відділі:\n", table)

    # 3. Відобразити всі проекти, які виконуються в обраному відділі (запит з параметром)
    selected_department = input("Введіть код відділу для перегляду проектів: ")
    cursor.execute(
        """
        SELECT p.project_number, p.name, p.deadline, p.budget
        FROM projects p
        JOIN project_executions pe ON p.id = pe.project_number_id
        JOIN departments d ON pe.department_code_id = d.id
        WHERE d.id = %s;
        """, (selected_department,)
    )
    table = PrettyTable(["Номер проекту", "Назва проекту", "Термін виконання", "Бюджет"])
    for row in cursor.fetchall():
        table.add_row(row)
    print(f"\nПроекти у відділі {selected_department}:\n", table)

    # 4. Порахувати кількість працівників у кожному відділі
    cursor.execute(
        """
        SELECT d.name AS department_name, COUNT(e.employee_code) AS num_workers
        FROM departments d
        LEFT JOIN employees e ON d.id = e.department_code_id
        GROUP BY d.name;
        """
    )
    table = PrettyTable(["Відділ", "Кількість працівників"])
    for row in cursor.fetchall():
        table.add_row(row)
    print("\nКількість працівників у кожному відділі:\n", table)

    # 5. Порахувати розмір премії для кожного співробітника (оклад * процент премії)
    cursor.execute(
        """
        SELECT e.last_name, e.first_name, p.salary, p.bonus_percent,
               (p.salary * p.bonus_percent / 100) AS bonus
        FROM employees e
        JOIN positions p ON e.position_code_id = p.id;
        """
    )
    table = PrettyTable(["Прізвище", "Ім'я", "Оклад", "Процент премії", "Розмір премії"])
    for row in cursor.fetchall():
        table.add_row(row)
    print("\nРозмір премії для кожного співробітника:\n", table)

    # 6. Порахувати кількість робітників з різним рівнем освіти у кожному відділі
    cursor.execute(
        """
        SELECT d.name AS department_name,
               SUM(CASE WHEN e.education = 'спеціальна' THEN 1 ELSE 0 END) AS special_education,
               SUM(CASE WHEN e.education = 'середня' THEN 1 ELSE 0 END) AS secondary_education,
               SUM(CASE WHEN e.education = 'вища' THEN 1 ELSE 0 END) AS higher_education
        FROM employees e
        JOIN departments d ON e.department_code_id = d.id
        GROUP BY d.name;
        """
    )
    table = PrettyTable(["Відділ", "Спеціальна освіта", "Середня освіта", "Вища освіта"])
    for row in cursor.fetchall():
        table.add_row(row)
    print("\nКількість робітників за рівнем освіти в кожному відділі:\n", table)

    # Закриття з'єднання
    cursor.close()
    connection.close()

if __name__ == "__main__":
    execute_queries()
