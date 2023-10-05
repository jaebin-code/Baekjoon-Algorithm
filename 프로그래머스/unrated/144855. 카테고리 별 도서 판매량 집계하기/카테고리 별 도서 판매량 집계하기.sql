# 22-1 도서 판매량 -> 카테고리, 총 판매량
SELECT b.category, sum(sales) as TOTAL_SALES FROM book as b
INNER JOIN book_sales as s on b.book_id = s.book_id
WHERE s.SALES_DATE LIKE "2022-01%"
GROUP BY b.category
ORDER BY b.category asc;
