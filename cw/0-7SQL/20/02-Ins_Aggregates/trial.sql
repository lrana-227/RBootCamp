SELECT * FROM ACTOR;
SELECT * FROM ADDRESS;
SELECT * FROM CITY;
SELECT * FROM COUNTRY;
SELECT * FROM CUSTOMER;
SELECT * FROM CUSTOMER_LIST;
SELECT * FROM FILM;
SELECT * FROM FILM_ACTOR;
SELECT * FROM INVENTORY;
SELECT * FROM PAYMENT;
SELECT * FROM RENTAL;
SELECT * FROM STAFF;
SELECT * FROM STORE;

SELECT rating, count(film_id)
FROM film
GROUP BY rating;
