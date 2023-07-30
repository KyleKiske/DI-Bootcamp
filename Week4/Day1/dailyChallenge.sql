CREATE TABLE actors(
	id serial primary key,
	first_name varchar(50),
	last_name varchar(100),
	age date,
	number_oscars smallint
);

INSERT INTO actors(first_name, last_name, age, number_oscars)
VALUES ('Matt', 'Damon', '1970-08-10', 5),
('George', 'Clooney', '1961-06-05', 2),
('Angelina', 'Jolie', '1975-06-04', 1),
('Jennifer', 'Aniston', '1969-02-11', 0);

select count(*) from actors

INSERT INTO actors(first_name, last_name, age, number_oscars)
VALUES ('Ryan', 'Gosling', '1980-11-12', 0);

select count(*) from actors;

INSERT INTO actors(first_name, last_name, number_oscars)
VALUES ('Cillian', 'Murphy',  0);

INSERT INTO actors(first_name, last_name, age)
VALUES ('Tim', 'Roth',  '1961-05-14');

INSERT INTO actors(first_name, age)
VALUES ('John', '1961-05-14');

select * from actors;