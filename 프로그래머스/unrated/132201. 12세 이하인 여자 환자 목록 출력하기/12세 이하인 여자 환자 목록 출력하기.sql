SELECT pt_name, pt_no, gend_cd, age, ifnull(tlno,'NONE') FROM patient
WHERE GEND_CD = 'W' and AGE <=12
ORDER BY AGE desc, pt_name asc;