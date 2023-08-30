SELECT f.flavor FROM first_half as f
INNER JOIN icecream_info as i on f.flavor=i.flavor
WHERE i.INGREDIENT_TYPE = 'fruit_based' and f.total_order>3000
order by f.total_order desc;