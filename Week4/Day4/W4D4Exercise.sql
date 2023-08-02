CREATE EXTENSION IF NOT EXISTS citext;  

CREATE TABLE menu_items(
	item_id SERIAL PRIMARY KEY,
	item_name citext NOT NULL unique,
	item_price SMALLINT DEFAULT 0
);