-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- );

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar');

-- SELECT * FROM FirstTab;

-- CREATE TABLE SecondTab (
--     id integer 
-- );

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL);

-- SELECT * FROM SecondTab;


SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL);
-- I think it will be 3.
-- Turned out to be zero, because one NULL != different NULL


SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
-- 	It would be 2 because NULL will never be IN or NOT in.


SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );
-- 	It would be 0 because NULL will destroy in statement.

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
--  It would be 2 because it's the same as second queation.
