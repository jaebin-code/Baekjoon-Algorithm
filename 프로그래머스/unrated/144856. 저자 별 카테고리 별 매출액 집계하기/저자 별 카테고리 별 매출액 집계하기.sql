#2022년 1월
SELECT book.AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(sales*price) as TOTAL_SALES FROM BOOK
LEFT JOIN author on book.author_id = author.author_id
LEFT JOIN book_sales on book.book_id = book_sales.book_id
WHERE sales_date like "2022-01%"
GROUP BY author_name, category
ORDER BY book.author_id asc, category desc;