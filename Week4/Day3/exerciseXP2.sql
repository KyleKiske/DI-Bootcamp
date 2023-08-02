-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
update film
set language_id = 2
where film_id in (133, 3);

-- Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table?
-- ADDRESS_ID

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
drop table customer_review;
-- Easy, because it has no childs.

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
select count(*) from rental
where return_date is null;

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
select title, replacement_cost
from film
join inventory on inventory.film_id = film.film_id
join rental on rental.inventory_id = inventory.inventory_id
order by replacement_cost desc
limit 30;

-- Your friend is at the store, and decides to rent a movie.
-- He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
select title from film 
join film_actor on film_actor.film_id = film.film_id
join actor on actor.actor_id = film_actor.actor_id
where actor.first_name = 'Penelope' and actor.last_name = 'Monroe'
and (film.description ilike('%sumo wrestler%'));

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
select title from film 
join film_category as fc on fc.film_id = film.film_id
join category on category.category_id = fc.category_id
where film.length < 60 and rating = 'R' and category.name ilike 'documentary%';

-- The 3rd film : A film that his friend Matthew Mahan rented. 
-- He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
select title from film
join inventory on inventory.film_id = film.film_id
join rental on rental.inventory_id = inventory.inventory_id
join customer on rental.customer_id = customer.customer_id
where rental.return_date between '2005-07-28' and '2005-08-1' and customer.first_name = 'Matthew'
and customer.last_name = 'Mahan' and film.rental_rate > 4;

-- The 4th film : His friend Matthew Mahan watched this film, as well.
-- It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
select title, replacement_cost from film
join inventory on inventory.film_id = film.film_id
join rental on rental.inventory_id = inventory.inventory_id
join customer on rental.customer_id = customer.customer_id
where customer.first_name = 'Matthew'
and customer.last_name = 'Mahan' and (film.description ilike('%boat%') or film.title ilike('%boat%'))
order by replacement_cost desc;