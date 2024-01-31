-- 회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력

-- MEMBER_PROFILE와 REST_REVIEW 테이블에서 
-- 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회

-- 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬

SELECT A.MEMBER_NAME, B.REVIEW_TEXT, date_format(B.REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
FROM MEMBER_PROFILE as A
    JOIN REST_REVIEW as B
    ON A.MEMBER_ID = B.MEMBER_ID
WHERE A.MEMBER_ID = (SELECT MEMBER_ID
                     FROM REST_REVIEW
                     GROUP BY MEMBER_ID
                     ORDER BY count(*) desc 
                     LIMIT 1)
                        
ORDER BY REVIEW_DATE, REVIEW_TEXT