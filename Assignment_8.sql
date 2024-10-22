

# question 1 

alter table rental 
add column status  varchar(50)


update rental
set status = 
	case
		when return_date > rental_date then 'late'
		when return_date < rental_date then 'early'
		when return_date = rental_date then 'on time'

	end

# question 2 

select city_id , sum(amount) as total_spent
from address 
join customer on address.address_id = customer.address_id
join payment on customer.customer_id = payment.customer_id
where city_id = 314 and city_id = 975
group by city_id

# question 3 

select category.name , count(film.film_id) as total_per_category
from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
group by category.name

# question 4 

	The are two different tables for catgory and film_category , because their need to be a way to connect the film and category tables attaching the category to the film.

# question 5 

select film.film_id , film.title,film.length 
from film
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.inventory_id
where return_date between '05-15-2005' and '05-31-2005' 

# question 6

select film.title , avg(amount) as below_avg
from payment 
join rental on payment.customer_id = rental.customer_id
join inventory on rental.inventory_id = inventory.inventory_id
join film on inventory.film_id = film.film_id
where payment.amount < (select avg(amount)from payment)
group by film.title

# question 7

select status , count(film.film_id) as film_count
from rental 
join inventory on rental.inventory_id = inventory.inventory_id
join film on inventory.film_id = film.film_id
group by status

# question 8 

select film.title,film.length, percent_rank() over (order by film.length) as percentile_rank
from film

# question 9

	The query from question 6 differs from question 7 , by the hashaggregates and the group key’s are different.For question 6’s query there is an init plan . These variations can have an impact on performance, with query 6 potentially being more resource-intensive due to the need for RAM to manage hash tables and the initial init plan. In contrast, query 7's window function may be more efficient in situations where row-by-row processing is preferable.

# extra credit 

-  The wrong relationship in the data is the staff_id being in rental because it does not correlate to the rental.
- Set-based programming, such as SQL, deals with entire sets of data at once, focusing on what to do (for example, filtering rows) rather than how to loop through them.Where as procedural programming like python is more step by step because your having to define everything.


	