import mysql.connector
from config import dbconfig_edit, dbconfig_read

def get_connection(db_name=None, read_db=False):
    """
    Создает и возвращает подключение к базе данных.
    :param db_name: Имя базы данных (по умолчанию None).
    :param read_db: Флаг для подключения к базе только для чтения (по умолчанию False).
    :return: Объект соединения или None в случае ошибки.
    """
    conn_params = dbconfig_read.copy() if read_db else dbconfig_edit.copy()

    if db_name:
        conn_params['database'] = db_name

    try:
        print(f"Подключение к базе данных: {conn_params.get('database', 'по умолчанию')}, режим: {'чтение' if read_db else 'запись'}")
        connection = mysql.connector.connect(**conn_params)
        return connection
    except mysql.connector.Error as err:
        print(f"Ошибка подключения к базе данных: {err}")
        return None

get_connection()