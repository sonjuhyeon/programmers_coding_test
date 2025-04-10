-- 코드를 입력하세요
SELECT REST_INFO.FOOD_TYPE, REST_ID, REST_NAME, FAVORITES FROM REST_INFO
JOIN
    (
        SELECT FOOD_TYPE, MAX(FAVORITES) AS MAX_F FROM REST_INFO
        GROUP BY FOOD_TYPE
    ) AS SUB
    ON
        SUB.FOOD_TYPE = REST_INFO.FOOD_TYPE AND
        SUB.MAX_F = REST_INFO.FAVORITES
ORDER BY FOOD_TYPE DESC