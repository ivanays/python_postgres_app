import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="db",
                                  port="5432",
                                  database="ivanayskiy")

    cursor_max = connection.cursor()
    cursor_min = connection.cursor()
    postgreSQL_select_Query_max = "SELECT MAX(age) FROM test_table WHERE LENGTH(name) < 6"
    postgreSQL_select_Query_min = "SELECT MIN(age) FROM test_table WHERE LENGTH(name) < 6"

    cursor_max.execute(postgreSQL_select_Query_max)
    cursor_min.execute(postgreSQL_select_Query_min)
   
    mobile_records_max = cursor_max.fetchall()
    mobile_records_min = cursor_min.fetchall()
 
    for row_max in mobile_records_max:
        print("Максимальный возраст для людей, длина имён которых меньше 6 символов равен: ", row_max[0], )

    for row_min in mobile_records_min:
        print("Минимальный возраст для людей, длина имён которых меньше 6 символов равен: ", row_min[0], )

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor_max.close()
        cursor_min.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")