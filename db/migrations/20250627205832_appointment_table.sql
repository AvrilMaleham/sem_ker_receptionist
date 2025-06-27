-- migrate:up
CREATE TABLE IF NOT EXISTS appointment (
    id SERIAL PRIMARY KEY,
    start_datetime TIMESTAMP,
    end_datetime TIMESTAMP,
    service_details TEXT,
    stylist_id INTEGER REFERENCES staff(id),
    customer_id INTEGER REFERENCES customer(id),
    noshow BOOLEAN,
    notes TEXT
);

CREATE INDEX IF NOT EXISTS idx_appointment_time ON appointment(start_datetime, end_datetime);

-- migrate:down
DROP INDEX IF EXISTS idx_appointment_time;
DROP TABLE IF EXISTS appointment;
