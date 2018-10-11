USE sakila;
SELECT * FROM actor;

SELECT first_name, last_name FROM actor;

SELECT UPPER(CONCAT(first_name, last_name)) AS 'Actor Name' FROM actor;

SELECT first_name,last_name FROM actor
	WHERE first_name = 'Joe';

SELECT first_name,last_name FROM actor
	WHERE last_name Like '%GEN%';

SELECT first_name,last_name FROM actor
	WHERE last_name Like '%LI%'
    ORDER BY last_name,first_name;

SELECT * FROM country;
SELECT country_id,country FROM country
	WHERE country IN ('Afghanistan','Bangladesh','China');

ALTER table actor ADD COLUMN description blob AFTER last_name;

ALTER TABLE actor DROP COLUMN description;

SELECT last_name, count(last_name) AS 'count' FROM actor
	GROUP BY last_name ASC;

SELECT last_name, count(last_name) AS 'count' FROM actor
	GROUP BY last_name ASC HAVING count(last_name) >=2;

UPDATE actor SET first_name='Harpo'
	WHERE first_name='GROUCHO' AND last_name='WILLIAMS';

UPDATE actor SET first_name='GROUCHO'
	WHERE first_name='Harpo' AND last_name='Williams';


SHOW CREATE TABLE address;

SELECT first_name, last_name, address FROM staff
	JOIN address ON staff.address_id = address.address_id;

SELECT first_name, last_name, SUM(amount) AS 'sum' FROM staff AS s
	INNER JOIN payment AS p ON s.staff_id = p.staff_id
    GROUP BY first_name;

SELECT title, COUNT(actor_id) FROM film AS f
	JOIN film_actor ON f.film_id = film_actor.film_id GROUP BY title;

SELECT title, COUNT(title) FROM film AS f
	JOIN inventory on f.film_id = inventory.film_id
	WHERE f.title='Hunchback Impossible';

SELECT last_name, first_name, SUM(amount) FROM customer AS c
	JOIN payment AS p ON c.customer_id = p.customer_id
    GROUP BY first_name, last_name ORDER BY last_name;

SELECT title FROM film
	WHERE title LIKE 'K%' OR title LIKE 'Q%'
    AND language_id IN (SELECT language_id FROM language WHERE name='English');

SELECT first_name, last_name FROM actor
	WHERE actor_id  IN (SELECT actor_id FROM film_actor WHERE film_id
					IN (SELECT film_id FROM film WHERE title='ALONE TRIP'));

SELECT first_name, last_name, email FROM customer AS c
	JOIN address AS a ON c.address_id = a.address_id
    JOIN city AS ct ON a.city_id=ct.city_id JOIN country as co ON ct.country_id=co.country_id;

SELECT title FROM film AS f 
	JOIN film_category AS fc ON f.film_id =fc.film_id
    JOIN category as c ON fc.category_id=c.category_id;

SELECT * FROM film;
SELECT title, COUNT(title) FROM film
	JOIN inventory ON film.film_id=inventory.film_id
    JOIN rental ON inventory.inventory_id=rental.inventory_id
    GROUP BY title ORDER BY COUNT(title) ASC;

SELECT * FROM payment;
SELECT store_id, SUM(amount) FROM payment AS p
	JOIN staff AS s ON p.staff_id=s.staff_id GROUP BY store_id;

SELECT store_id, city, country FROM store s
	JOIN address a ON s.address_id=a.address_id
    JOIN city ct ON s.address_id=a.address_id
    JOIN country c ON ct.country_id=c.country_id;

SELECT name, SUM(amount) FROM category
	JOIN film_category ON category.category_id=film_category.category_id
    JOIN inventory ON film_category.film_id=inventory.film_id
    JOIN rental ON inventory.inventory_id=rental.inventory_id
    JOIN payment ON rental.rental_id=payment.rental_id
    GROUP BY category.name
    ORDER BY SUM(amount) DESC LIMIT 5;

create view top_five_genres AS
SELECT name AS "genres", SUM(amount) FROM category 
	JOIN film_category ON category.category_id=film_category.category_id
    JOIN inventory ON film_category.film_id=inventory.film_id
    JOIN rental ON inventory.inventory_id=rental.inventory_id
    JOIN payment ON rental.rental_id=payment.rental_id
    GROUP BY category.name
    ORDER BY SUM(amount) DESC LIMIT 5;
    

SELECT * FROM top_five_genres;

DROP VIEW top_five_genres;