Data Engineer Assessment Writeup

#Setting up postgres server, database, and table
pg_ctl -D /usr/local/var/postgres start

CREATE DATABASE test;

CREATE TABLE account (
index bigint,
account_number int,
customer_name text,
effective_date date,
balance numeric(12,2),
status text
);

#login to psql test database
$ psql -d test
