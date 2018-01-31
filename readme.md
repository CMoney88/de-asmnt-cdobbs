

#Setting up postgres server, database, and table




#login to psql test database
$ psql -d test

# Data Engineer Assessment Writeup

Please review the cameron-de.py file provided in this repo. It has a custom connection to a local postgres database. If you want to run this script yourself, please modify the engine variable with the appropriate connection properties.

## General Approach

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Data Considerations

asdfasdf

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
