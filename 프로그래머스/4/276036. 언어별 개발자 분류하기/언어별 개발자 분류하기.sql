-- 코드를 작성해주세요
WITH FRONT_SKILL AS (
    SELECT CODE AS CODE, 'C' AS GR
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
),
C_HASH_SKILL AS (
    SELECT CODE, 'B' AS GR
    FROM SKILLCODES
    WHERE NAME = 'C#'
),
FRONT_PYTHON AS (
    SELECT
        CODE + PYTHON AS CODE, 'A' AS GR
    FROM SKILLCODES
    JOIN (
        SELECT CODE AS PYTHON FROM SKILLCODES
        WHERE NAME = 'Python'
    ) PY
    WHERE CATEGORY = 'Front End'
),
GRADE_CODE AS (
    SELECT * FROM FRONT_SKILL
    UNION ALL
    SELECT * FROM C_HASH_SKILL
    UNION ALL
    SELECT * FROM FRONT_PYTHON
),
MATCH_GRADE AS (
    SELECT
        D.*,
        GC.GR,
        ROW_NUMBER() OVER (
            PARTITION BY D.ID
            ORDER BY
            CASE GC.GR
                WHEN 'A' THEN 1
                WHEN 'B' THEN 2
                WHEN 'C' THEN 3
            END
        ) AS RN
    FROM DEVELOPERS D
    JOIN GRADE_CODE GC ON D.SKILL_CODE & GC.CODE = GC.CODE
)
SELECT GR AS GRADE, ID, EMAIL FROM MATCH_GRADE
WHERE RN = 1
ORDER BY GRADE, ID