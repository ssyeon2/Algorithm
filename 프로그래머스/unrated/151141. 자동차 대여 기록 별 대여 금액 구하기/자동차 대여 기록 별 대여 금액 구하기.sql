-- 코드를 입력하세요
SELECT HISTORY_ID,
    round(DAILY_FEE  *
      (CASE
      WHEN DATEDIFF(END_DATE, START_DATE)+1 < 7 THEN 1
      WHEN DATEDIFF(END_DATE, START_DATE)+1 < 30 THEN 0.95
      WHEN DATEDIFF(END_DATE, START_DATE)+1 < 90 THEN 0.92
      ELSE 0.85 END )
    * (DATEDIFF(his.END_DATE, his.START_DATE)+1)) AS FEE
      
FROM CAR_RENTAL_COMPANY_CAR AS CAR 
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS HIS
    ON CAR.CAR_ID = HIS.CAR_ID
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS DIS
    ON CAR.CAR_TYPE = DIS.CAR_TYPE
    
WHERE CAR.CAR_TYPE = '트럭'

GROUP BY HISTORY_ID

ORDER BY FEE DESC, HISTORY_ID DESC