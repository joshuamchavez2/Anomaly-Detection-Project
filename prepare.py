import pandas as pd
import numpy as np
from datetime import timedelta, datetime

def clean(df):
    
    # using a map to make more sense of the values
    df['program'] = df.program_id.map({1:"php", 2:"java", 3:"ds", 4:"fe"})
    
    # dropped deleted_at since all values are null
    df = df.drop(columns=['deleted_at'])
    
    # Filtering out the fields where cohort_id is null
    df = df[~df.cohort_id.isnull()]
    
    # filtering out just a single null value in path
    df = df[~df.path.isna()]
    
    # Combining date and time
    df['request_date_time'] = df.date + " " + df.time
    
    # Converting date type object to datetime64
    df.request_date_time = pd.to_datetime(df.request_date_time)
    
    df['date_year'] = df.request_date_time.dt.year
    df['date_month'] = df.request_date_time.dt.month_name()
    df['date_weekday'] = df.request_date_time.dt.day_name()
    df['hour'] = df.request_date_time.dt.hour
    
    df = df.drop(columns=['date', 'time', 'cohort_id', 'id', 'slack','program_id'])
    
    
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['updated_at'] = pd.to_datetime(df['updated_at'])
    
    # Thanks Josh B. for this
    df['url'] = df['path'].str.split('/').str[0]

    # Thanks Josh B. for this
    df['lesson'] = df['path'].str.split('/').str[1]

    df['lesson'] = np.where(df.lesson.isnull(), 'no data', df.lesson)
    
    df = df[df.name != 'Staff']

    df = df[df.path != '/']

    # Data Science URL lesson merging
    df['url'] = np.where(df['url'] == '1-fundamentals', 'fundamentals', df['url'])
    df['url'] = np.where(df['url'] == '3-sql', 'sql', df['url'])
    df['url'] = np.where(df['url'] == '4-python', 'python', df['url'])
    df['url'] = np.where(df['url'] == '6-regression', 'regression', df['url'])
    df['url'] = np.where(df['url'] == '5-stats', 'stats', df['url'])
    df['url'] = np.where(df['url'] == '10-anomaly-detection', 'anomaly-detection', df['url'])
    df['url'] = np.where(df['url'] == '8-clustering', 'clustering', df['url'])
    df['url'] = np.where(df['url'] == '7-classification', 'classification', df['url'])
    df['url'] = np.where(df['url'] == '2-storytelling', 'storytelling', df['url'])
    df['url'] = np.where(df['url'] == '11-nlp', 'nlp', df['url'])
    df['url'] = np.where(df['url'] == '9-timeseries', 'timeseries', df['url'])

    # Web Dev URL lesson merging
    df['url'] = np.where(df['url'] == 'javascript-i', 'java-i', df['url'])
    df['url'] = np.where(df['url'] == 'javascript-ii', 'java-ii', df['url'])
    df['url'] = np.where(df['url'] == 'javascript-iii', 'java-iii', df['url'])
    
    return df

def prepare(df):
    df = clean(df)
    return df