(SELECT u.name AS results
FROM MovieRating AS m, users AS u
WHERE m.user_id = u.user_id
GROUP BY m.user_id
-- COUNT(m.user_id) is num of movies this user rated, in descending order
ORDER BY COUNT(m.user_id) DESC, u.name LIMIT 1)
UNION ALL
(SELECT m.title AS results
FROM movies AS m, MovieRating AS r
-- first filter what we need
WHERE r.movie_id = m.movie_id
AND r.created_at like '2020-02-%'
-- then group and calculate
GROUP BY r.movie_id
-- first one will be highest rating move title
ORDER BY AVG(r.rating) DESC, m.title limit 1)
