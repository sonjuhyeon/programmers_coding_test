-- 코드를 작성해주세요
/*
SELECT
    ID,
    CASE
        WHEN NTILE(4) OVER (ORDER BY SIZE_OF_COLONY) = 1 THEN 'LOW'
        WHEN NTILE(4) OVER (ORDER BY SIZE_OF_COLONY) = 2 THEN 'MEDIUM'
        WHEN NTILE(4) OVER (ORDER BY SIZE_OF_COLONY) = 3 THEN 'HIGH'
        ELSE 'CRITICAL'
    END AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID
*/

SELECT
    ID,
    CASE
        WHEN PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY) <= 0.25 THEN 'LOW'
        WHEN PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY) <= 0.5 THEN 'MEDIUM'
        WHEN PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY) <= 0.75 THEN 'HIGH'
        ELSE 'CRITICAL'
    END AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID
