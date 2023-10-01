-- 코드를 입력하세요
SELECT i.INGREDIENT_TYPE , SUM(TOTAL_ORDER) as TOTAL_ORDER FROM FIRST_HALF as f
INNER JOIN icecream_info as i on f.flavor = i.flavor
GROUP BY i.ingredient_type
ORDER BY TOTAL_ORDER asc;