import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def process_data(engine, num):
    conn = engine.connect()

    max = pd.read_sql('SELECT MAX(age) FROM test_table WHERE LENGTH(name) < 6', conn)
    min = pd.read_sql('SELECT MIN(age) FROM test_table WHERE LENGTH(name) < 6', conn)

    if num == 1:
        return max
    elif num == 2:
        return min


if __name__ == "__main__":
    db_user = 'postgres'
    db_password = 'password'
    db_host = 'db'
    db_port = '5432'
    db_name = 'ivanayskiy'

    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    result_max = process_data(engine,1)
    result_min = process_data(engine,2)

    print("Максимальный возраст для людей, длина имён которых меньше 6 символов равен: ")
    print(result_max)
    print("Минимальный возраст для людей, длина имён которых меньше 6 символов равен: ")
    print(result_min)