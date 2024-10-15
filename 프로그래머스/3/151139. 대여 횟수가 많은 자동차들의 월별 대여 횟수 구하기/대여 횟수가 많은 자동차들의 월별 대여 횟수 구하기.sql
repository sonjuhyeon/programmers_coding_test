-- 코드를 입력하세요
SELECT
    MONTH(start_date) AS MONTH,
    car_id,
    COUNT(car_id) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(start_date, '%y-%m') BETWEEN '22-08' AND '22-10'
    AND car_id IN(SELECT car_id
                 FROM   car_rental_company_rental_history
                 WHERE  start_date BETWEEN '2022-08-01' AND '2022-10-31'
                 GROUP  BY car_id
                 HAVING Count(*) >= 5)
GROUP BY car_id, MONTH
ORDER BY MONTH, car_id DESC