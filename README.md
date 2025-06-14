Project Overview

This project demonstrates a ETL pipeline where google sheet is used as the data source, and the final output is stored in AWS S3 as a Parquet file. 
The entire process is orchestrated using Apache Airflow and automated to run on a daily schedule.

Technologies Used
1. Google Sheet (via gspread library)
2. Python (Data processing & transformation)
3. Pandas (Dataframe manipulation)
4. Apache Airflow (Workflow orchestration)
5. AWS S3 (Cloud storage)
6. Parquet (File format)

Steps Implemented

Google Sheet Creation

A google sheet was created via Gmail, with the following columns:

first name
Last namE
 State of Origin 

Data Population

The sheet was populated with names of class participants. 
The “State of Origin” field was filled with random values for demonstration purposes.

Data Retrieval and Cleaning

Using the gspread library, data was retrieved from the google sheet. 
Before processing, column names were formatted by converting to lowercase, whitespace was trimmed and
words in column headers were replaced with underscores (e.g., "First Name" to first_name).

Data Transformation and Storage

The cleaned data was converted into a Pandas DataFrame.
It was then saved in Parquet format for optimal storage and querying.

Data Upload to S3

A dedicated S3 bucket was created for storing the processed data.
The Parquet file was uploaded into the bucket.
Workflow Automation with Airflow.
A custom Airflow DAG was built to automate the pipeline.
The DAG is scheduled to run daily.

It includes tasks for fetching, formatting, storing, and uploading the data.

