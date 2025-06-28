-- migrate:up
ALTER TABLE customer ADD COLUMN card_num text;

-- migrate:down
ALTER TABLE customer DROP COLUMN card_num;
