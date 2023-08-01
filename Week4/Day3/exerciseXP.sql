-- 1. Get a list of all film languages.
select name from language;


-- 2. Get a list of all films joined with their languages – select the following details:
-- film title, description, and language name.
select f.title, f.description, l.name from film as f
join language as l on f.language_id = l.language_id;

--  Try your query with different joins:
-- 2.1. Get all films, even if they don’t have languages.
select f.title, f.description, l.name from film as f
left join language as l on f.language_id = l.language_id;
-- 2.2. Get all languages, even if there are no films in those languages.
select f.title, f.description, l.name from film as f
right join language as l on f.language_id = l.language_id;


-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
create table new_film (
	id serial primary key,
	name varchar(30) not null
);

insert into new_film(name)
values 
('Drunken Master'),
('All Quiet on the Western Front'),
('Ghost in the Shell');


-- 4. Create a new table called customer_review, which will contain film reviews that customers will make.
create table customer_review(
	review_id serial primary key,
	film_id integer references new_film(id) on delete cascade,
	language_id integer references language(language_id),
	title varchar(30) not null,
	score smallint check(between 1 and 10),
	review_text text not null,
	last_update date
);

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
insert into customer_review(film_id, language_id, title, score, review_text, last_update)
values (2, 6, 'The harsh reality of WWI', 7, 'HUGE TEXT', '2023-03-16'),
 	(3, 3, 'What future are we heading to?', 9, 'HUGE TEXT ABOUT DYSTOPIA', '2018-04-18');


-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
delete from new_film where id = 2;

-- The review for movie 2 will be gone
select * from customer_review;