# run "/opt/airflow/start.sh" command to start the web server.

import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def fn_hello():

    logging.info("Hello Vivian")


def fn_addition():
    logging.info(f"2 + 2 = {2+2}")


def fn_subtraction():
    logging.info(f"6 -2 = {6-2}")


def fn_division():
    logging.info(f"10 / 2 = {int(10/2)}")


dag1 = DAG(
    "lesson1.exercise3",
    schedule_interval='@hourly',
    start_date=datetime.datetime.now() - datetime.timedelta(days=1))

hello_task = PythonOperator(
    task_id="hello",
    python_callable=fn_hello,
    dag=dag1)

#
# TODO: Define an addition task that calls the `addition` function above
#
addition_task = PythonOperator(
    task_id="addition",
    python_callable=fn_addition,
    dag=dag1)
#
# TODO: Define a subtraction task that calls the `subtraction` function above
#
subtraction_task = PythonOperator(
    task_id="subtraction",
    python_callable=fn_subtraction,
    dag=dag1)
#
#
# TODO: Define a division task that calls the `division` function above
#
division_task = PythonOperator(
    task_id="division",
    python_callable=fn_division,
    dag=dag1)
#
# TODO: Configure the task dependencies such that the graph looks like the following:
#
#                    ->  addition_task
#                   /                 \
#   hello_world_task                   -> division_task
#                   \                 /
#                    ->subtraction_task

hello_task >> addition_task
hello_task >> subtraction_task
addition_task  >> division_task
subtraction_task  >> division_task
