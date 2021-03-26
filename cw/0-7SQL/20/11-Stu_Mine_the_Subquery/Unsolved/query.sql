Select first_name, last_name from actor
WHERE actor_id in (
	Select actor_id from film_actor
	WHERE film_id  in (
		Select film_id FROM film
		WHERE film.title = 'ALTER VICTORY')
)
