# задание 3.6  + pro задания
# перед выполнением добавить переменную file4numeros = "/opt/airflow/app/numeros.txt"

# перед выполнением добавить переменную connection_id = "conn1"
# добавить соединение conn1 к локальной базе postgres port 5431, ip 172.17.0.1

# перед выполнением добавить переменную connection_id = "conn2"
# добавить соединение conn1 к локальной базе postgres port 5430, ip 172.17.0.1


from datetime import datetime, timedelta
from random import randint
from pathlib import Path
import subprocess
import psycopg2

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.base import BaseHook

from airflow.sensors.python import PythonSensor

# аргументы дага по умолчанию
default_args = {
    'owner':'peter',
    'retries':5,
    'retry_delay': timedelta(minutes=1)
}

# функция выбора ветки
def _pick_branch(**context):
    if isFileCorrect() == True:
        return "task_create_table"
    else:
        return "task_exception"

def task_create_table(**context):
    file_name = Variable.get("file4numeros")
    hook = PostgresHook(postgres_conn_id="conn2")
    # запрос sql
    sql_request = f'CREATE TABLE IF NOT EXISTS table1 (id serial PRIMARY KEY, val1 integer, val2 integer);'
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute(sql_request)

    # c. чтение сгенерированных чисел из файла
    with open(file_name, "r+") as f:
        for line in f.readlines():
            split = line.strip().split(" ")
            if len(split) > 1:
                val1, val2 = split
                cursor.execute("INSERT INTO table1 (val1, val2) VALUES (%s, %s)", (val1, val2))
    conn.commit()
    cursor.close()
    conn.close()

    print("TASK CREATE TABLE BEGIN!!!! ")

def task_exception(**context):
    print("!!!!!  ERROR DATA !!!!! ")


# функция проверяет сформированный файл на корректность
def isFileCorrect():

    if not isFileExists():
        return False

    isCorrect = True
    # путь к папке с файлом хранится в настройках airflow
    # Admin->Variables
    file_name = Variable.get("file4numeros")

    #  удаление предыдущего значения сумм 
    # (удаление последней строки в файле - командой linux)
    subprocess.run(['sed','-i','$ d',file_name])

    try:

        # c. чтение сгенерированных чисел и подстчет сумм
        with open(file_name, "r+") as f:
            for line in f.readlines():
                line.strip().split(" ")

    except Exception as e:
        isCorrect = False
    
    print(f'isFileCorrect - {isCorrect}')
    return isCorrect

# функция проверки существования файла
def isFileExists():
    file_path = Path(Variable.get("file4numeros"))
    return file_path.exists()

# Функция задает условия сенcора 12g
def wait_for_sensors():
    # начальная иницилизация переменных
    summa1, summa2, res, countsDagRun,countsStr, x = 0,0,0,0,0,0
    isExistFile, isCountsRun, isCorrectCalc = False, False, False

    # проверка существования файла
    isExistFile = isFileExists()
    
    # **** проверка на количество запусков dag ****

    # определим количество запусков dag
    countsDagRun = getCountsOfRunDag('sensor12')

    # определим количество строк в файле
    countsStr = getCountStr()

    if (countsDagRun == countsStr):
        isCountsRun = True

    print(f'Количество запусков dag: {countsDagRun}')
    print(f'Количество строк в файле: {countsStr}')
    print(f'is CountsRun -  {isCountsRun}')
    print(f'is ExistsFile -  {isExistFile}')


    if (isExistFile and isCountsRun):
        return True
    else:
        return False


# Функция, возвращает объект соединения к postgres
# conn_id - соединение
def get_connection_toPostgres(conn_id) -> BaseHook.get_connection:
    conn = BaseHook.get_connection(conn_id)
    return conn

# Функция возвращает количество запусков daga dag_id 
def getCountsOfRunDag(dag_id):
    hook = PostgresHook(postgres_conn_id="conn1")
    # запрос sql
    sql_request = f'SELECT COUNT(*) FROM dag_run WHERE dag_id=\'{dag_id}\''

    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute(sql_request)
    data = cursor.fetchall()
    for row in data:
        row = " ".join(map(str, row))
    cursor.close()
    conn.close()
    return int(row)

# функция возвращает количество строк в файле -1 последняя
def getCountStr():

    file_name = Variable.get("file4numeros")
    # используется команда linux wc -l filename
    completed = subprocess.run(['wc', '-l',file_name], stdout=subprocess.PIPE)
    count = int(completed.stdout.decode('utf-8').split(" ")[0])-1  
    return count



# генерация 2х чисел. 
# сгенерированные числа должны записываться в текстовый файл – через пробел. 
# При этом должно соблюдаться условие, что каждые новые два числа должны 
# записываться с новой строки не затирая предыдущие.
def generate_dos_numeros():

    val1 = randint(0,100)
    val2 = randint(0,100)

    print(f'primera value: {val1}, segunda value: {val2}')

    # путь к папке с файлом хранится в настройках airflow
    # Admin->Variables
    file_name = Variable.get("file4numeros")
    #file_name = "/opt/airflow/app/numeros.txt"

    #  удаление предыдущего значения сумм 
    # (удаление последней строки в файле - командой linux)
    subprocess.run(['sed','-i','$ d',file_name])


    # c. Запись сгенерированных чисел в файл
    with open(file_name, "a+") as f:
        f.write(f'{val1} {val2} \n')

# функция подсчета сумм числе в файле
def calculation_numeros ():
    file_name = Variable.get("file4numeros")

    # cумма первой колонки
    suma1 = 0
    # cумма второй колонки
    suma2 = 0

    # c. чтение сгенерированных чисел и подстчет сумм
    with open(file_name, "r+") as f:
        for line in f.readlines():
            val1, val2 = line.strip().split(" ")
            suma1 += int(val1)
            suma2 += int(val2)
            print(f'Numeros: {val1}, {val2}')

        print(f'suma1: {suma1}, suma2: {suma2}')
        f.write(f'{suma2-suma1} \n')

# A DAG represents a workflow, a collection of tasks
with DAG (
    default_args = default_args,
    dag_id = "sensor12",
    schedule_interval = "1-5 * * * *",
    max_active_runs = 5,
    start_date = datetime(2023, 1, 25),
    end_date = datetime(2023, 2, 15),
    catchup=False
) as dag:

    task_start = BashOperator(
        task_id='start_task',
        bash_command= "echo Airflow запускает задачи...",
        do_xcom_push=False # отключаем вывод в xcom
    )

    task_end = BashOperator(
        task_id='end_task',
        bash_command= "echo Airflow выполнило задачи...",
        do_xcom_push=False
    )


    # # Task задания генерации чисел
    task_generate_numeros = PythonOperator(
        task_id='generate_numeros', 
        python_callable = generate_dos_numeros,
        do_xcom_push=False
    )

    # # Task задания подсчета сумм
    task_calculate_numeros = PythonOperator(
        task_id="calculate_numeros", 
        python_callable = calculation_numeros,
        do_xcom_push=False
    )

    wait_for_sensor = PythonSensor(
        task_id='check_file',
        python_callable=wait_for_sensors,
        poke_interval=15,
        timeout=300,
        mode="reschedule"
    )

    # оператор выбора ветки
    pick_branch = BranchPythonOperator(
        task_id='pick_branch',
        python_callable=_pick_branch
    )

    task_create_table = PythonOperator(
        task_id='task_create_table', 
        python_callable = task_create_table,
        do_xcom_push=False
    )

    task_exception = PythonOperator(
        task_id='task_exception', 
        python_callable = task_exception,
        do_xcom_push=False
    )



    # полная цепочка операторов по заданию
    task_start >> task_generate_numeros >> task_calculate_numeros >> \
    wait_for_sensor >> pick_branch >> [task_create_table, task_exception] >> task_end

    # генерация чисел
    #task_start >> task_generate_numeros >> task_calculate_numeros >> task_end