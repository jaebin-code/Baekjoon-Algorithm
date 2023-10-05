# 총금액 70만원 이상 -> ID, nickname,  total_cost
SELECT USER_ID, NICKNAME, SUM(PRICE) as TOTAL_SALES FROM used_goods_board as b
INNER JOIN used_goods_user as f ON f.user_id = b.writer_id
WHERE status = "done"
GROUP BY USER_ID, nickname
HAVING SUM(PRICE) >= 700000
ORDER BY SUM(PRICE) ASC;