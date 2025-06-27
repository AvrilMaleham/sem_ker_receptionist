-- migrate:up
CREATE TABLE IF NOT EXISTS customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    address TEXT,
    phone_number VARCHAR(15),
    email VARCHAR(100)
);

CREATE INDEX IF NOT EXISTS idx_customer_name ON customer(first_name, last_name);

-- migrate:down
DROP INDEX IF EXISTS idx_customer_name;
DROP TABLE IF EXISTS customer;

