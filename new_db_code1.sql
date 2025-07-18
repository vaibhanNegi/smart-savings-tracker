CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(150),
    monthly_income FLOAT,
    savings_amount FLOAT,
    spending_amount FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
drop table auth_users;


CREATE TABLE auth_users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(150) UNIQUE,
    password VARCHAR(100)
);

select * from auth_users;


