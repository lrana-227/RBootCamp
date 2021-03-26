-- 1. What is the average cost to rent a film in the stores?
SELECT ROUND(AVG(rental_rate),2) as "Average Rental Rate" from film;

-- 2. What is the average rental cost of films by rating? On average, what is the cheapest rating of films to rent? Most expensive?
SELECT RATING, AVG(RENTAL_RATE) AS "AVERAGE Rental/Rating" from film 

GROUP BY RATING

-- 3. How much would it cost to replace all the films in the database?


-- 4. How much would it cost to replace all the films in each ratings category?


-- 5. How long is the longest movie in the database? The shortest?
