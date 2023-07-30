CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

INSERT INTO actors(first_name, last_name, age, number_oscars)
VALUES ('Matt', 'Damon', '1970-08-10', 5),
('George', 'Clooney', '1961-06-05', 2),
('Angelina', 'Jolie', '1975-06-04', 1),
('Jennifer', 'Aniston', '1969-02-11', 0);

select count(*) from actors;

INSERT INTO actors(first_name, last_name, age, number_oscars)
VALUES ('Ryan', 'Gosling', '1980-11-12', 0);

select count(*) from actors;

-- INSERT INTO actors(first_name, last_name, number_oscars)
-- VALUES ('Cillian', 'Murphy',  0);

-- INSERT INTO actors(first_name, last_name, age)
-- VALUES ('Tim', 'Roth',  '1961-05-14');

-- INSERT INTO actors(first_name, age)
-- VALUES ('John', '1961-05-14');
-- Commented lines won't work since all columns set to not null

select * from actors;