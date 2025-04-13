-- 코드를 입력하세요
SELECT
    A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY,
    SUM(BS.SALES * B.PRICE) AS TOTAL_SALES
FROM BOOK B
JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
JOIN BOOK_SALES BS ON B.BOOK_ID = BS.BOOK_ID
WHERE SALES_DATE LIKE '2022-01%'
GROUP BY A.AUTHOR_ID, B.CATEGORY
ORDER BY A.AUTHOR_ID, B.CATEGORY DESC