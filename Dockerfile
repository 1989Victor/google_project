FROM apache/airflow:2.10.5

WORKDIR /new_app/

COPY requirements.txt /new_app/
COPY service_account.json /opt/airflow/


RUN pip install -r requirements.txt 