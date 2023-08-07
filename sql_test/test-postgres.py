import psycopg2
from psycopg2 import Error, sql

DATABASE = "test_db"
USER = "postgres"
PASSWORD = "88888888"
LOCALHOST = "127.0.0.1"
PORT = "5432"

READ_VERSION = "SELECT version();"
READ_TABLE_NAMES = '''
select 
  (select r.relname from pg_class r where r.oid = c.conrelid) as table, 
  (select array_agg(attname) from pg_attribute 
   where attrelid = c.conrelid and ARRAY[attnum] <@ c.conkey) as col, 
  (select r.relname from pg_class r where r.oid = c.confrelid) as ftable 
from pg_constraint c;
'''

READ_ALL_OPERATIONS = '''SELECT * FROM %s;'''

CREAT_TABLE_DIABETES = '''
  CREATE TABLE IF NOT EXISTS diabet (
    Person_id SERIAL PRIMARY KEY,
    Person_name VARCHAR(100),
    Pregnancies INTEGER,
    Glucose INTEGER,
    BloodPressure INTEGER,
    SkinThickness INTEGER,
    Insulin INTEGER,
    BMI DOUBLE PRECISION,
    DiabetesPedigreeFunction DOUBLE PRECISION,
    Age INTEGER,
    Outcome INTEGER
  );

'''

INSERT_DIABET_DATA = """INSERT INTO diabet (Insulin, BMI) VALUES (%s, %s)"""

try:
    connection = psycopg2.connect(dbname="test_db", user=USER, password=PASSWORD, host=LOCALHOST, port=PORT)
    curs = connection.cursor()

    print("Информация по подключению")
    print(connection.get_dsn_parameters())

    curs.execute(CREAT_TABLE_DIABETES)

    curs.execute(INSERT_DIABET_DATA, (4, 56.7))

    database = 'diabet'
    sql = READ_ALL_OPERATIONS % database

    print(sql)

    curs.execute(sql)

    record = curs.fetchone()
    print(f"Текущая запись {record}")

    # curs.execute(READ_TABLE_NAMES)
    # print(f"Перечень таблиц в БД {curs.fetchall()}")

    # curs.execute(READ_ALL_OPERATIONS)
    # data = curs.fetchall()

    # print(f"Данные таблицы operations {curs.fetchall()}")

except(Exception, Error) as error:
    print("Возникло исключение при работе с Postgres", error)
