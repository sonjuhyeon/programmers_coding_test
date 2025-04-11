-- 코드를 작성해주세요
# SELECT
#     SUM(SCORE) AS SCORE,
#     HE.EMP_NO,
#     HE.EMP_NAME,
#     HE.POSITION,
#     HE.EMAIL
# FROM HR_EMPLOYEES HE
# JOIN HR_GRADE HG ON HE.EMP_NO = HG.EMP_NO
# GROUP BY HE.EMP_NO
# ORDER BY SCORE DESC
# LIMIT 1

SELECT
    SUM(SCORE) AS SCORE,
    HE.EMP_NO,
    HE.EMP_NAME,
    HE.POSITION,
    HE.EMAIL
FROM HR_EMPLOYEES HE
JOIN HR_GRADE HG ON HE.EMP_NO = HG.EMP_NO
GROUP BY HE.EMP_NO
HAVING SUM(HG.SCORE) = (
    SELECT MAX(SUM_SCORE) FROM (
        SELECT SUM(SCORE) AS SUM_SCORE
        FROM HR_GRADE
        GROUP BY EMP_NO
    ) AS TMP
)