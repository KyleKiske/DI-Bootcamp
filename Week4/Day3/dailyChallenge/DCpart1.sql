create table customer (
	id serial primary key,
	first_name varchar(30),
	last_name varchar(30) not null
);

create table customer_profile (
	id serial primary key,
	isLoggedIn boolean DEFAULT false,
	customer_id integer references customer(id) unique
);

insert into customer(first_name, last_name)
values ('John', 'Doe'),
	('Jerome', 'Lalu'),
	('Lea', 'Rive');
	
insert into customer_profile(customer_id, isLoggedIn)
values ((select id from customer where first_name = 'John'), FALSE),
	((select id from customer where first_name = 'Jerome'), TRUE);

select first_name from customer as C
join customer_profile as P on p.customer_id = c.id
where p.isLoggedIn = TRUE;

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
select first_name, isLoggedIn from customer as C
left join customer_profile as P on p.customer_id = c.id;

-- The number of customers that are not LoggedIn
select count(first_name) from customer as C
left join customer_profile as P on p.customer_id = c.id
where isLoggedIn <> TRUE;