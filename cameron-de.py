import boto3
import StringIO
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

#Connect to public S3 bucket
s3 = boto3.resource('s3')
debucket = s3.Bucket('data-engineer-assessment')

#Load inputfile into memory using StringIO
inputfile = StringIO.StringIO()
debucket.download_fileobj('InputFile.dat', inputfile)

#Create a simple string
newStr = inputfile.getvalue()

#Create a list by splitting the string on newline
newList = newStr.split('\n')

#Create a dataframe by splitting each row by the delimiter for each item in the list
df = pd.DataFrame([sub.split('|') for sub in newList])

#Rename the dataframe columns and drop the header row
df = df.rename(columns={0:'AccountNumber', 1:'Key', 2:'Value'})
df = df.drop(0)

#Pivot the dataframe so that the keys become columns
dfpivot = df.pivot(index='AccountNumber', columns = 'Key', values = 'Value')

#Reset index so that AccountNumber is no longer the index
dfpivot2 = dfpivot.reset_index()

#Replace string characters
dfpivot2['Balance'] = dfpivot2['Balance'] = dfpivot2['Balance'].str.replace(r'[$, ]','')
dfpivot2['Balance'] = dfpivot2['Balance'] = dfpivot2['Balance'].str.replace('-','0')
dfpivot2['Balance'] = dfpivot2['Balance'] = dfpivot2['Balance'].str.replace('NULL','0')

#Filter data set to only 2 rows to insert into table
dfpivot2 = dfpivot2.loc[[0,5]]

#Convert the columns to the proper datatypes to allow for insert into postgres schema
dfpivot2['Balance'] = dfpivot2['Balance'].astype(float)
dfpivot2['AccountNumber'] = dfpivot2['AccountNumber'].astype(int)
dfpivot2['EffectiveDate'] = pd.to_datetime(dfpivot2['EffectiveDate'])

#Rename columns to match postgres table schema
dfpivot3 = dfpivot2.rename(columns={
'AccountNumber':'account_number',
'CustomerName':'customer_name',
'EffectiveDate':'effective_date',
'Status':'status',
'Balance':'balance'})

#Create postgres connection
engine = create_engine('postgresql://cdobbs@localhost:5432/test')

#Write dataframe to existing postgres table
dfpivot3.to_sql('account', engine, if_exists='append')
