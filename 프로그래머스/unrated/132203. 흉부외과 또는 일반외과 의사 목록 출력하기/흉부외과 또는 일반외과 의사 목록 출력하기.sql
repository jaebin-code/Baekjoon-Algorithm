SELECT dr_name, dr_id, mcdp_cd, LEFT(hire_ymd,10) FROM DOCTOR
WHERE mcdp_cd = "CS" or mcdp_cd = "GS"
ORDER BY hire_ymd desc, dr_name asc;