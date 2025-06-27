-- migrate:up
CREATE TABLE IF NOT EXISTS service (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    cost NUMERIC(10,2),
    duration INTERVAL,
    related_services TEXT
);

CREATE INDEX IF NOT EXISTS idx_service_name ON service(name);

-- migrate:down
DROP INDEX IF EXISTS idx_service_name;
DROP TABLE IF EXISTS service;

