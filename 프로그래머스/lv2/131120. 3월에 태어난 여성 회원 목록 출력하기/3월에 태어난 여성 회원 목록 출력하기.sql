SELECT member_id,member_name,gender,left(date_of_birth,10)
FROM MEMBER_PROFILE
WHERE GENDER = 'W' and substr(DATE_OF_BIRTH,7)=3 and TLNO is not null
order by member_id asc