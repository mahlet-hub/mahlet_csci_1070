--question 1
select *
from customer
where last_name like 'T%'
order by last_name ASC
--question 2
select *
from rental
where return_date between '2005-05-28' and '2005-06-01';
--question 3 
--I would use the count query too determine which film was rented most.
select f.title, count(r.rental_id) as rental_count
from rental r
join inventory i on r.inventory_id = i.inventory_id
join film f on i.film_id = f.film_id
group by f.title
order by rental_count DESC
limit 10
--question 4
select c.customer_id, c.first_name, c.last_name, SUM(p.amount) AS total_spent
join customer 
join rental on c.customer_id = r.customer_id
join payment on r.rental_id = p.rental_id
group by c.customer_id, c.first_name, c.last_name
order by total_spent ASC
--question 5 
select actor.first_name, actor.last_name, film.release_year
from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
--question 6
-- for question 4 , I used the select query to choose what columns I wanted to be displayed 
-- I used the join query to go into the cutsomer table , the rental and payment
-- then I used the on query to connect the .customer_id and rental_id to the both of the tables
-- then I used the group by query to group the output by customer_id , last name and first name
-- I used the order by query to list the output by the amount from least to most
-- for question 5 , I used the select query to select what columns I wanted to be displayed
-- I used the from query so that the information would be from the film data table
-- I used the join query to join the film_actor and actor table and the on query to connect the two cloumns
--question 7 
select c.name, avg(f.rental_rate) as avg_rental_rate
from film f
join film_category fc on f.film_id = fc.film_id
join category c on c.category_id = fc.category_id
group by c.category_id, c.name
--question 8
select c.name as category_name, count(r.rental_id) as total_rentals, sum(p.amount) as total_sales
from rental r
join inventory i on r.inventory_id = i.inventory_id
join film f on i.film_id = f.film_id
join film_category fc on f.film_id = fc.film_id
join category c on fc.category_id = c.category_id
join payment p on r.rental_id = p.rental_id
group by c.category_id, c.name
order by total_rentals DESC
limit 5
