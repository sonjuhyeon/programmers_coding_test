SELECT 
    YEAR(e.DIFFERENTIATION_DATE) AS "YEAR",
    (m.max - e.SIZE_OF_COLONY) AS "YEAR_DEV",
    e.ID
FROM 
    ECOLI_DATA e
JOIN 
    (SELECT 
         YEAR(DIFFERENTIATION_DATE) AS "y",
         MAX(SIZE_OF_COLONY) AS "max"
     FROM 
         ECOLI_DATA
     GROUP BY 
         YEAR(DIFFERENTIATION_DATE)
    ) m 
ON 
    YEAR(e.DIFFERENTIATION_DATE) = m.y
ORDER BY 
    1, 2;