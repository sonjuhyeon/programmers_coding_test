-- 코드를 입력하세요
SELECT
    YEAR(SALES_DATE) AS YEAR,
    MONTH(SALES_DATE) AS MONTH,
    GENDER,
    COUNT(DISTINCT UI.USER_ID) AS USERS
FROM USER_INFO UI
JOIN ONLINE_SALE OS ON UI.USER_ID = OS.USER_ID
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER
HAVING GENDER IS NOT NULL
ORDER BY YEAR, MONTH, GENDER