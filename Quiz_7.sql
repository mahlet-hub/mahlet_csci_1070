--question 1 
select *
from payment 
where amount >= 9.99

--question 2 part 1 
select max(amount)
from payment

-- question 2 part 2 
select *
from film
where replacement_cost = 11.99

--question 3
select first_name , last_name , email , staff.address_id , city , country 
from staff
join address on staff.address_id = address.address_id
join city on address.city_id = city.city_id
join country on city.country_id = country.country_id 

--question 4 
-- Companies such as apple or google seem like they would give me a decent amount of money .

--question 5 (extra credit)
-- the crow foot notation between country and city contains the same "country_id" that correlates the two. 





