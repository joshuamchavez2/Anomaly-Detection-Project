import pandas as pd
import numpy as np
import os

from env import host, user, password

def get_db_url(url):
    url = f'mysql+pymysql://{user}:{password}@{host}/{url}'
    return url

def data():
    '''
    This function reads the curriculum_logs data from the Codeup db into a df,
    write it to a csv file, and returns the df.
    '''
    sql_query = """
                SELECT *
                FROM logs
                LEFT JOIN cohorts
                    ON logs.cohort_id = cohorts.id;
                """

    df = pd.read_sql(sql_query, get_db_url('curriculum_logs'))

    return df

def acquire():
    '''
    This function reads in curriculum_logs data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('logs.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('logs.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = data()
        
        # Write DataFrame to a csv file.
        df.to_csv('logs.csv')
        
    return df