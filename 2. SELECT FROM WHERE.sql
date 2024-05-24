-- SELECT <field name> FROM <table name> WHERE <conditions>;
USE sqldb;
SELECT * FROM usertbl;

-- Basic WHERE
SELECT * FROM usertbl WHERE name = '김경호';

-- Relational Op.
-- =, <, >, <=, >=, <>, !=, etc.
-- NOT, AND, OR, etc.
SELECT userID, Name FROM usertbl WHERE birthYear >= 1970 AND height >= 182;
SELECT userID, Name FROM usertbl WHERE birthYear >= 1970 OR height >= 182;

-- BETWEEN ... AND, IN(), LIKE
SELECT name, height FROM usertbl WHERE height BETWEEN 180 AND 183; -- Can use continuous variable only
SELECT name, addr FROM usertbl WHERE addr = '경남' OR addr = '전남' OR addr = '경북'; -- Can use not only continuous ones but also discrete ones
