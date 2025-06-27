-- migrate:up
CREATE TABLE IF NOT EXISTS purchase_history (
    transaction_id SERIAL,
    customer_id INTEGER REFERENCES customer(id),
    product_id INTEGER REFERENCES product(id),
    staff_id INTEGER REFERENCES staff(id),
    nbr_items INTEGER,
    datetime TIMESTAMP,
    PRIMARY KEY (transaction_id, product_id)
);

CREATE INDEX IF NOT EXISTS idx_purchase_history_customer_id ON purchase_history(customer_id);

-- migrate:down
DROP INDEX IF EXISTS idx_purchase_history_customer_id;
DROP TABLE IF EXISTS purchase_history;
