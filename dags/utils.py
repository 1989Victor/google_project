import awswrangler as wr
import boto3
import pandas as pd
import gspread
from datetime import datetime
from airflow.models import Variable

session = boto3.Session(
    aws_access_key_id = Variable.get('ACCESS_KEY'),
    aws_secret_access_key = Variable.get('SECRET_KEY'),
    region_name='us-east-2'
)



def get_results():
    """
    To fetch the data from the goooglesheet.
    """
    gc = gspread.service_account("/opt/airflow/service_account.json")
    sh = gc.open("Group_names")
    worksheet = sh.sheet1
    all_data = worksheet.get_all_records()
    return all_data


def convert_all_data(all_data):
    """
    Convert the extracted data to Dataframe and format. 
    """
    all_data_new = pd.DataFrame.from_dict(all_data)
    
    new_columns = []
    
    for col in all_data_new.columns:
        # To convert to lower case
        col = col.lower()
        # To trim the whitespace
        col = col.strip()
        # To separate with underscore
        col = col.replace(" ", "_")
        new_columns.append(col)
    all_data_new.columns = new_columns
    return all_data_new

def load_df_to_s3(df):
    """"
    Load the dataframe to s3 bucket.
    """
    s3_pathway = "s3://victor-gspread-bucket/google_sheet_folder/Group_names.parquet"
    wr.s3.to_parquet(
                 df=df,
                 path=s3_pathway,
                 index=False,
                 boto3_session=session,
                 dataset=False
                )


print("successfully uploaded")


def full_pipeline():
    """
    Extract, transform and load.
    """
    extract = get_results()
    transform = convert_all_data(extract)
    load_df_to_s3(transform)

print("Successfull")
