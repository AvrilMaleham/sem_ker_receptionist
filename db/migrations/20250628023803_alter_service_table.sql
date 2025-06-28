-- migrate:up
ALTER TABLE service ADD COLUMN skill_level text;

-- migrate:down
ALTER TABLE service DROP COLUMN skill_level;

