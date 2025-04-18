-- 코드를 입력하세요
SELECT DISTINCT CRCC.CAR_ID FROM CAR_RENTAL_COMPANY_CAR CRCC
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY CRCRH ON CRCC.CAR_ID = CRCRH.CAR_ID
WHERE
    CAR_TYPE = '세단' AND
    DATE_FORMAT(START_DATE, '%m') = 10
ORDER BY CRCC.CAR_ID DESC