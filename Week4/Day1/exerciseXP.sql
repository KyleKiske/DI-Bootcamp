CREATE TABLE items(
	id serial primary key,
	name varchar(80),
	price integer
);

INSERT INTO items(name, price) 
VALUES ('Small Desk', 100),
 	('Large Desk', 300),
  	('Fan', 80);
	
CREATE TABLE customers(
	id serial primary key,
	name varchar(15),
	last_name varchar(25)
);

INSERT INTO customers(name, last_name)
VALUES 
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie','Johnson');

select * from items;

select * from items
WHERE price > 80;

select * from items
WHERE price <= 300;

select * from customers
WHERE last_name = 'Smith';

select * from customers
WHERE last_name = 'Jones';

select * from customers
WHERE not last_name = 'Scott';
