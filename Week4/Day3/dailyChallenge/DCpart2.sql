create table book 
(
	book_id SERIAL PRIMARY KEY, 
	title varchar(50) NOT NULL, 
	author varchar(30) NOT NULL
);

Insert into book(title, author)
values ('Alice In Wonderland', 'Lewis Carroll'),
	('Harry Potter', 'J.K Rowling'),
	('To kill a mockingbird', 'Harper Lee');

Create table Student(
	student_id SERIAL PRIMARY KEY,
	name varchar(30) NOT NULL UNIQUE,
	age smallint check(age <= 15)
);	

Insert into Student(name, age)
values ('John', 12),
	('Lera', 11),
	('Patrick', 10),
	('Bob', 14);

create table Library (
	book_fk_id integer references book(book_id) ON DELETE CASCADE ON UPDATE CASCADE ,
	student_id integer references student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
	borrowed_date date,
	PRIMARY KEY (book_fk_id, student_id)
);

insert into Library(student_id, book_fk_id, borrowed_date)
values ((select student_id from student where name = 'John'), (select book_id from book where title = 'Alice In Wonderland'), '2022-02-15'),
((select student_id from student where name = 'Bob'), (select book_id from book where title = 'To kill a mockingbird'), '2021-03-03'),
((select student_id from student where name = 'Lera'), (select book_id from book where title = 'Alice In Wonderland'), '2021-05-23'),
((select student_id from student where name = 'Bob'), (select book_id from book where title = 'Harry Potter'), '2021-08-12');

select * from Library;

select s.name, b.title from Student s
join library l on l.student_id = s.student_id 
join book b on l.book_fk_id = b.book_id;

select avg(age) from student s
join library l on l.student_id = s.student_id 
join book b on l.book_fk_id = b.book_id
where b.title = 'Alice In Wonderland';

delete from student
where name = 'John';