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
--I would use this query to determine which movies are rented the most :
select title, count(rental.rental_id) as rental_count
from film
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.inventory_id
group by title
order by rental_count desc
--question 3 part 2 
select title, count(rental.rental_id) as rental_count
from film
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.inventory_id
group by title
order by rental_count desc
limit 10 
--question 4 
select customer.customer_id, customer.first_name, customer.last_name, sum(payment.amount) as total_payed
from customer
join rental on customer.customer_id = rental.customer_id
join payment on rental.rental_id = payment.rental_id 
group by customer.customer_id ,customer.first_name , customer.last_name 
order by total_payed desc
--question 5
select actor.actor_id, actor.first_name, actor.last_name , COUNT(film.film_id) AS movie_count
join actor
join film_actor on actor.actor_id = film_actor.actor_id
join film on film_actor.film_id = film.film_id
where film.release_year = 2006
group by actor.actor_id, actor.first_name, actor.last_name
order by movie_count desc
--question 6
-- for question 4 , I used select to choose what columns I wanted to be displayed 
-- I used  join  to go into the cutsomer table , the rental and payment
-- then I used on to connect the .customer_id and rental_id to the both of the tables
-- then I used group by to group the output by customer_id , last name and first name
-- I used order by to list the output by the amount 
-- for question 5 , I used  select to select what columns I wanted to be displayed
-- I used  from  so that the information would be from the film data table
-- I used join to match the film_actor and actor table and on to connect the two columns
—question 7 
select category.name  , avg(film.rental_rate) as avg_rental_rate
from category
join film_category on category.category_id = film_category.category_id 
join film on film_category.film_id = film.film_id 
group by category.name
—question 8
select category.name , count(rental.rental_id) as rental_count , sum(payment.amount) as total_sales
from category
join film_category on category.category_id = film_category.category_id 
join film on film_category.film_id = film.film_id 
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.inventory_id
join payment on rental.rental_id = payment.rental_id
group by category.name
order by total_sales desc
—extra credit
select category.name as category_name, 
       TO_CHAR(rental.rental_date, 'Month') as month, 
       count(rental.rental_id) as rental_count
from category
join film_category on category.category_id = film_category.category_id
join film on film_category.film_id = film.film_id
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.inventory_id
group by category.name, TO_CHAR(rental.rental_date, 'Month')
order by month, category_name 





