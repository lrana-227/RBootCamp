
CREATE VIEW title_inventory as 
SELECT title, count(inventory.film_id) as film_count FROM FILM
INNER JOIN inventory on 
film.film_id = inventory.film_id
group by title
order by film_count DESC


SELECT * FROM title_inventory