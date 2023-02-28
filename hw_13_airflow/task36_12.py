# задание 3.6  п.12 a-f (когорта light)


from datetime import datetime, timedelta
from random import randint
from pathlib import Path
import subprocess

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator

# аргументы дага по умолчанию
default_args = {
    'owner':'peter',
    'retries':5,
    'retry_delay': timedelta(minutes=1)
}



def hello():
    print("Hello Airflow!")

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
    file_name = file_name = Variable.get("file4numeros")

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
# генерация
dag = DAG(
    default_args = default_args,
    dag_id = "12gen_dag_v01",
    schedule_interval = "1-5 * * * *",
    max_active_runs = 5,
    start_date = datetime(2023, 1, 13),
    end_date = datetime(2023, 1, 17),
    catchup=False
)

# Tasks are represented as operators
bash_task = BashOperator(
    task_id="hello", 
    bash_command="echo hello",
    dag=dag
)

python_task_word = PythonOperator(
    task_id="world", 
    python_callable = hello
)

# Task задания генерации чисел
python_task_generate_numeros = PythonOperator(
    task_id="generate_numeros", 
    python_callable = generate_dos_numeros
)

# Task задания подсчета сумм
python_task_calculate_numeros = PythonOperator(
    task_id="calculate_numeros", 
    python_callable = calculation_numeros
)



# Set dependencies between tasks
bash_task >> python_task_word >> python_task_generate_numeros >> python_task_calculate_numeros