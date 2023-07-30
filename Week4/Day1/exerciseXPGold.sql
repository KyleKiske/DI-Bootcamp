CREATE TABLE students(
	id serial primary key,
	last_name varchar(25),
	first_name varchar(25),
	birth_date date
);

INSERT INTO students(first_name, last_name, birth_date)
VALUES 
('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea', 'Benichou',	'1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson',	'1980-10-03');

select * from students;

select first_name, last_name from students;

select first_name, last_name from students
WHERE id = 2;

select first_name, last_name from students
WHERE last_name = 'Benichou' AND first_name = 'Marc';

select first_name, last_name from students
WHERE last_name = 'Benichou' OR first_name = 'Marc';

select first_name, last_name from students
WHERE LOWER(first_name) like '%a%';

select first_name, last_name from students
WHERE LOWER(first_name) like 'a%';

select first_name, last_name from students
WHERE LOWER(first_name) like '%a';

select first_name, last_name from students
WHERE LOWER(first_name) like '%a_';

select first_name, last_name from students
WHERE id = 1 or id = 3;

select * from students
WHERE birth_date > '2000-01-01';

select first_name, last_name, birth_date from students 
ORDER BY last_name ASC
LIMIT 4;

select first_name, last_name, birth_date from students 
ORDER BY birth_date DESC
LIMIT 1;

select first_name, last_name, birth_date from students 
WHERE id > 2
LIMIT 3;