--to find a column NOT IN other column, use sub query
SELECT employee_id
FROM (
    SELECT employee_id, manager_id
    FROM Employees
    WHERE salary < 30000
) em_ma_subque
WHERE manager_id NOT IN (SELECT DISTINCT employee_id FROM employees)
ORDER BY employee_id
