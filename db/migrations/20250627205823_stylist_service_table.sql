-- migrate:up
CREATE TABLE IF NOT EXISTS stylist_service (
    stylist_id INTEGER REFERENCES staff(id),
    service_id INTEGER REFERENCES service(id),
    PRIMARY KEY (stylist_id, service_id)
);

-- migrate:down
DROP TABLE IF EXISTS stylist_service;
