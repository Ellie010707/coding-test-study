-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, date_format(HIRE_YMD, "%Y-%m-%d") as HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD like "%CS%"
    or MCDP_CD like "%GS%"
ORDER BY HIRE_YMD desc, DR_NAME
