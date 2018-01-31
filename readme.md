
# Data Engineer Assessment Writeup

Please review the cameron-de.py file provided in this repo. I have provided several comments to provide context to the code.

It has a custom connection to a local postgres database. If you want to run this script locally, please modify the engine variable with the appropriate connection properties.

## General Approach

I loaded the inputfile.dat into a public S3 bucket to act as a typical source dataset that would be worked with on a project.

This file was download and then loaded into memory. Various transformations were then applied to the dataset to convert it to string, then list, then finally a dataframe so I could manipulate the columns and rows appropriately.

I performed a pivot, reindex, column renaming, string replacement, and datatype casting on the dataframe.

Lastly, I filtered the set to the desired 2 row output and inserted it into an EXISTING postgres table with a defined schema.

## Data Considerations

The datatypes I defined for the dataset was based on familiarity with the provided column (Key) names. One assumption that was necessary was the formatting of effective_date for account_number 1006; it could be either MM/DD/YYYY or DD/MM/YYYY format within knowing which one for certain.

### Postgres Setup
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
