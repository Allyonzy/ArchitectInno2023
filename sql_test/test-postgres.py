import psycopg2
from psycopg2 import Error, sql

DATABASE = "demo"
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

SET_PATH = '''SET search_path = bookings;'''

READ_DEMO_BOARDING_INFO = '''
select
	'Без посадочного талона' as "Статус брони",
	COUNT(b.book_ref) AS "Количество броней"
FROM bookings b
JOIN tickets t ON t.book_ref = b.book_ref
LEFT JOIN boarding_passes bp ON bp.ticket_no = t.ticket_no
WHERE bp.boarding_no IS null;
'''

READ_DEMO_BOARDING_INFO_FULL = '''
with find_model as (
	select 
		f.flight_no, 
		f.aircraft_code, 
		a.model
	from flights f
	join aircrafts a on a.aircraft_code = f.aircraft_code
)

select		fv.flight_no as "Номер рейса",
			fm.model as "Тип самолета",
			fv.scheduled_departure::date as "Плановая дата",
			fv.scheduled_departure::time as "Плановое время",
			fv.scheduled_arrival::date as "Плановая дата вылета",
			fv.scheduled_arrival::time as "Плановое время вылета",
			fv.scheduled_duration as "Длительность полета",			
			fv.departure_city as "Город отправления",
			fv.departure_airport as "Аэропорт"

from flights_v fv
join find_model fm on fm.flight_no = fv.flight_no
limit 20;
'''

try:
    connection = psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=LOCALHOST, port=PORT)
    curs = connection.cursor()

    print("Информация по подключению")
    print(connection.get_dsn_parameters())

    # curs.execute(CREAT_TABLE_DIABETES)

    # curs.execute(INSERT_DIABET_DATA, (4, 56.7))

    # database = 'diabet'
    # sql = READ_ALL_OPERATIONS % database

    # print(sql)

    curs.execute(SET_PATH)
    curs.execute(READ_DEMO_BOARDING_INFO_FULL)

    record = curs.fetchall() # для одной записи fetchone()

    print(f"Текущая запись {record}") # что выгрузилось

    # TODO преобразовать в читабельный вид (пример - текст с форматом или *DataFrame)
    #('PG0001', 'Bombardier CRJ-200', datetime.date(2016, 9, 19), datetime.time(14, 15), datetime.date(2016, 9, 19)

    # curs.execute(READ_TABLE_NAMES)
    # print(f"Перечень таблиц в БД {curs.fetchall()}")

    # curs.execute(READ_ALL_OPERATIONS)
    # data = curs.fetchall()

    # print(f"Данные таблицы operations {curs.fetchall()}")

except(Exception, Error) as error:
    print("Возникло исключение при работе с Postgres", error)
