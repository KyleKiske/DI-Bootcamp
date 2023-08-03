create table country(
	id serial primary key,
	name varchar(50) unique,
	capital varchar(30),
	flag varchar(50),
	subregion varchar(50),
	population integer not null
);