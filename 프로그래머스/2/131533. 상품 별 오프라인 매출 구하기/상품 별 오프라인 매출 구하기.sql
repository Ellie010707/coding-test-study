-- 상품코드 별 매출액(판매가 * 판매량) 합계를 출력
-- 매출액을 기준으로 내림차순 정렬
-- 상품코드를 기준으로 오름차순 정렬

SELECT p.PRODUCT_CODE, (o.SALES_AMOUNT * p.PRICE) as SALES
FROM PRODUCT as p
JOIN (SELECT PRODUCT_ID, sum(SALES_AMOUNT) as SALES_AMOUNT
        FROM OFFLINE_SALE
        GROUP BY PRODUCT_ID) as o
on p.PRODUCT_ID = o.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE

