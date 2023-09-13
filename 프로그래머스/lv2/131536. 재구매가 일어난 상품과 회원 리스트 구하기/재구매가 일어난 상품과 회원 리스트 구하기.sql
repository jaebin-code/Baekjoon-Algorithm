SELECT user_id, product_id FROM online_sale
group by user_id, product_id
having count(user_id)>1
order by user_id asc, product_id desc;