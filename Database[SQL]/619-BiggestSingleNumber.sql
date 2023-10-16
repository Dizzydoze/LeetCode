--Every derived table must have its own alias
-- SELECT sth from (whole result)
SELECT MAX(num) AS num
FROM(
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS unique_numbers
