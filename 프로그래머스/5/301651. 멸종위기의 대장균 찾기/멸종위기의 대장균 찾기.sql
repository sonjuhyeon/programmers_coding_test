-- 코드를 작성해주세요
WITH RECURSIVE GENERATION AS(
    SELECT ID, 1 AS G_LEVEL
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL # 최상위 노드

    UNION ALL

    SELECT E.ID, G.G_LEVEL + 1 AS G_LEVEL
    FROM ECOLI_DATA E
    INNER JOIN GENERATION G
    ON E.PARENT_ID = G.ID
)
SELECT
    COUNT(*) AS COUNT,
    G_LEVEL AS GENERATION
FROM GENERATION G
LEFT JOIN ECOLI_DATA E ON G.ID = E.PARENT_ID
WHERE E.ID IS NULL
GROUP BY GENERATION
ORDER BY GENERATION