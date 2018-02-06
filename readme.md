
# Data Engineer Assessment Writeup

Please review the cameron-de.py file provided in this repo. I have provided several comments to provide context to the code.

It has a custom connection to a local postgres database. If you want to run this script locally, please modify the engine variable with the appropriate connection properties.

## General Approach

I downloaded the SampleFile.dat from the public S3 bucket and then loaded into memory. Various transformations were then applied to the dataset to convert it to string, then list, then finally a dataframe so I could manipulate the columns and rows appropriately.

I performed a pivot, reindex, column renaming, string replacement, and datatype casting on the dataframe.

Lastly, I filtered the set to the desired 2 row output and inserted it into an EXISTING postgres table with a defined schema.

## Data Considerations

The datatypes I defined for the dataset was based on familiarity with the provided column (Key) names. For example, the balance column is typically a monetary value so a float datatype worked best. For effective_date, this is obviously a date format but with a mix of formatting and timestamps.

In order to convert the balance column to a float type I had to remove several string and spacing characters. This would make this field suspect in the future and a more programatic approach to cleanse this data is needed. Also, handling NULL string value presented a challenge and further called into question the source data.

One assumption that was necessary was the formatting of effective_date for account_number 106; it could be either MM/DD/YYYY or DD/MM/YYYY format without knowing which one for certain. Other values provided for effective_date were tenuous and would need further clarification in order to capture the correct information.

## Postgres Setup
Start a local postgres server:
```
pg_ctl -D /usr/local/var/postgres start
```

Create a database and table with native super-user:
```
CREATE DATABASE test;

CREATE TABLE account (
index bigint,
account_number int,
customer_name text,
effective_date date,
balance numeric(12,2),
status text
);
```
