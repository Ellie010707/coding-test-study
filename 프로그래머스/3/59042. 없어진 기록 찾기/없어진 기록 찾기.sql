-- 동물의 ID와 이름
-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물
-- ID 순으로 조회하는 SQL문을 작성해주세요.

# SELECT ANIMAL_ID, NAME
# FROM ANIMAL_OUTS 
# WHERE ANIMAL_ID not in (SELECT O.ANIMAL_ID
#                         FROM ANIMAL_OUTS as O
#                         JOIN ANIMAL_INS as I
#                         ON O.ANIMAL_ID = I.ANIMAL_ID)
                        
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS as O
LEFT JOIN ANIMAL_INS as I
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID is NULL