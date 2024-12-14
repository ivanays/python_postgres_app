import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="db",
                                  port="5432",
                                  database="ivanayskiy")

    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT MAX(age), MIN(age) FROM test_table WHERE LENGTH(name) < 6"

    cursor.execute(postgreSQL_select_Query)
   
    mobile_records = cursor.fetchall()
 
    for row in mobile_records:
        print("Максимальный возраст для людей, длина имён которых меньше 6 символов равен: ", row[0], )
        print("Минимальный возраст для людей, длина имён которых меньше 6 символов равен: ", row[1], )

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")