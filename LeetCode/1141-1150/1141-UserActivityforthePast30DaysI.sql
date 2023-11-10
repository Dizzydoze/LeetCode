--step by step, SELECT all we needed, FILTER the columns, GROUP as we needed
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM
    Activity
WHERE
    activity_type <> ''
AND
    activity_date > "2019-06-27" AND activity_date <= "2019-07-27"
GROUP BY
    activity_date
