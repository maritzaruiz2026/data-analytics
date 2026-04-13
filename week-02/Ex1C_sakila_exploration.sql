/*
a) Under Tables > actor > Columns you see the following: actor_id, first_name, last_name, and last_update.
b) Under Tabled > film > Columns you see the following: film_id, title, description, relrease_year, language_id, original_language, rental_duration, rental_rate, length, replacement_cost, rating, speacial_features, and last_update.
c) The table that contains both actor_id and film_id is film_actor. 
d) The rental table includes rows that contain rental_id, rental_date, inventory_id, customer_id, return_date, staff_id and last_update. The information is easy to read but it would be easier if dates and times were shortened.
e) The inventory table includes rows that contain inventory_id, film_id, store_id, and last_update.
f) The table I would need to use to understand the names of all films that were rented on a specific date would be tables film, inventory and rental. Film's table uses it's PK of film_id and it's connected as a FK under the inventory table. The rental table would be a bridge table that connects information from both the inventory and film table.
*/

SELECT film_id, title FROM film;
SELECT film_id, inventory_id FROM inventory;
SELECT rental_date, inventory_id FROM rental;