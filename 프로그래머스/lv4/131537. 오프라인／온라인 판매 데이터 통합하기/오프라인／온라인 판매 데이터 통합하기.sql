SELECT LEFT(o.sales_date,10) as date,o.product_id,o.user_id,o.sales_amount FROM online_sale as o
WHERE LEFT(o.sales_date,7)='2022-03'

UNION ALL

SELECT LEFT(f.sales_date,10) as date,f.product_id,null,f.sales_amount FROM offline_sale as f
WHERE LEFT(f.sales_date,7)='2022-03'

ORDER BY date asc, product_id asc, user_id asc;