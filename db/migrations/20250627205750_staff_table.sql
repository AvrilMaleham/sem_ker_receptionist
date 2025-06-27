-- migrate:up
CREATE TABLE IF NOT EXISTS staff (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    address TEXT,
    phone_number VARCHAR(15),
    email VARCHAR(100),
    staff_type VARCHAR(50)
);

CREATE INDEX IF NOT EXISTS idx_staff_name ON staff(first_name, last_name);

-- migrate:down
DROP INDEX IF EXISTS idx_staff_name;
DROP TABLE IF EXISTS staff;
