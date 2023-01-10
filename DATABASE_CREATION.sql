create database Network1;
use Network1;
CREATE TABLE DATA_TABLE(
	USERNAME varchar(45) NOT NULL,
	PASSWORD varchar(35) NOT NULL,
    LOGIN_DATE_TIME varchar(35) NOT NULL,
    IP_ADDRESS varchar(35)
);
drop table login;

select * from DATA_TABLE;
