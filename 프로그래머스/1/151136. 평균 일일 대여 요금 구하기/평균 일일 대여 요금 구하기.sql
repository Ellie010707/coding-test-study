-- 코드를 입력하세요
SELECT round(avg(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE LIKE 'SUV'