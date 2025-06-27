-- migrate:up
CREATE TABLE IF NOT EXISTS product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    brand VARCHAR(100),
    volume NUMERIC(10,2),
    unit VARCHAR(10),
    retail_price NUMERIC(10,2)
);

CREATE INDEX IF NOT EXISTS idx_product_name ON product(name);

-- migrate:down
DROP INDEX IF EXISTS idx_product_name;
DROP TABLE IF EXISTS product;
