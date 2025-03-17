import mysql.connector
from config import dbconfig


def get_connection(db_name=None):
    conn_params = dbconfig.copy()
    if db_name:
        conn_params['database'] = db_name
    return mysql.connector.connect(**conn_params)


def create_database_and_tables():
    with get_connection() as conn, conn.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS job_listings")
        print("База данных job_listings проверена/создана.")

    with get_connection('job_listings') as conn, conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Organizations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                url VARCHAR(1000)
            )""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Vacancies (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                url VARCHAR(1000) NOT NULL,
                salary VARCHAR(255),
                city VARCHAR(255),
                site_url VARCHAR(255),
                vacancy VARCHAR(2000),
                organization_id INT,
                FOREIGN KEY (organization_id) REFERENCES Organizations(id)
            )""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS VacancyTags (
                id INT AUTO_INCREMENT PRIMARY KEY,
                vacancy_id INT NOT NULL,
                tag VARCHAR(255) NOT NULL,
                FOREIGN KEY (vacancy_id) REFERENCES Vacancies(id)
            )""")

        conn.commit()
        print("Таблицы Organizations, Vacancies и VacancyTags проверены/созданы.")


def get_organization_id(cursor, name, url):
    cursor.execute("SELECT id FROM Organizations WHERE name = %s AND url = %s", (name, url))
    row = cursor.fetchone()
    return row[0] if row else None


def get_vacancy_id(cursor, url):
    cursor.execute("SELECT id FROM Vacancies WHERE url = %s", (url,))
    row = cursor.fetchone()
    return row[0] if row else None


def insert_tags(cursor, vacancy_id, tags):
    if tags:
        for tag in tags:
            cursor.execute("INSERT INTO VacancyTags (vacancy_id, tag) VALUES (%s, %s)", (vacancy_id, tag))


def insert_vacancy(data: dict):
    # create_database_and_tables()

    with get_connection('job_listings') as conn, conn.cursor() as cursor:
        org_name = data['company']['name']
        org_url = data['company']['url']
        organization_id = get_organization_id(cursor, org_name, org_url)

        if organization_id is None:
            cursor.execute("INSERT INTO Organizations (name, url) VALUES (%s, %s)", (org_name, org_url))
            organization_id = cursor.lastrowid

        vac_url = data['url']
        vacancy_id = get_vacancy_id(cursor, vac_url)

        if vacancy_id is None:
            cursor.execute("""
                INSERT INTO Vacancies (title, url, salary, city, site_url, vacancy, organization_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (data['title'], vac_url, data['salary'], data.get('city'),
                 data.get('site_url'), data.get('vacancy'), organization_id))

            vacancy_id = cursor.lastrowid
            insert_tags(cursor, vacancy_id, data.get('tags', []))
            conn.commit()
            print("Вакансия и связанные данные (теги) успешно добавлены в БД.")
        else:
            print("Вакансия с таким URL уже существует. Пропускаем вставку.")




if __name__ == '__main__':
    create_database_and_tables()
    example_data = {
        'title': "Пример вакансия",
        'url': "https://hh.ru/vacancy/123456",
        'salary': "до 100000 RUB",
        'tags': ["Python", "Django", "MySQL"],
        'company': {
            'name': "ООО Пример",
            'url': "https://hh.ru/employer/98765"
        },
        'city': "Москва",
        'site_url': "hh.ru",
        'vacancy': "Поиск Python-разработчика"
    }

    insert_vacancy(example_data)