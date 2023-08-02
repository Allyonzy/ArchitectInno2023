import psycopg2
from psycopg2 import Error

READ_VERSION = "SELECT version();"
READ_TABLE_NAMES = '''
select 
  (select r.relname from pg_class r where r.oid = c.conrelid) as table, 
  (select array_agg(attname) from pg_attribute 
   where attrelid = c.conrelid and ARRAY[attnum] <@ c.conkey) as col, 
  (select r.relname from pg_class r where r.oid = c.confrelid) as ftable 
from pg_constraint c;
'''

READ_ALL_OPERATIONS = '''SELECT * FROM operations;'''

try:
    connection = psycopg2.connect(dbname="test_db", user="postgres", password="88888888", host="127.0.0.1", port="5432")
    curs = connection.cursor()

    print("Информация по подключению")
    print(connection.get_dsn_parameters())

    curs.execute(READ_VERSION)

    record = curs.fetchone()
    print(f"Текущая запись {record}")

    curs.execute(READ_TABLE_NAMES)
    print(f"Перечень таблиц в БД {curs.fetchall()}")

    curs.execute(READ_ALL_OPERATIONS)
    data = curs.fetchall()

    print(f"Данные таблицы operations {curs.fetchall()}")

except(Exception, Error) as error:
    print("Возникло исключение при работе с Postgres", error)
