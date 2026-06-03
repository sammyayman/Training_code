-- -- Active: 1747240760303@@127.0.0.1@3305@ayman
-- SELECT
--     name AS database_name,
--     database_id,
--     create_date
-- FROM
--     sys.databases
-- ORDER BY
--     name;




-- EXEC sp_databases;

-- USE master;
-- GO

-- DROP DATABASE IF EXISTS SonicDB;



-- USE master;
-- GO

-- -- Check if the database exists
-- IF EXISTS (SELECT name FROM sys.databases WHERE name = 'SonicDB')
-- BEGIN
--     -- Drop the database
--     DROP DATABASE mydatabase;
-- END


-- CREATE DATABASE Ayman;




-- DROP DATABASE Ayman;

-- CREATE TABLE mytable (
--     id INT PRIMARY KEY,
--     name VARCHAR(50),
--     age INT,
--     is_active BIT,
--     created_date DATETIME,
--     salary MONEY,
--     description NVARCHAR(100),
--     image VARBINARY(MAX),
--     address GEOGRAPHY,
--     latitude FLOAT,
--     longitude FLOAT
-- );

-- SELECT * FROM mytable;

-- CREATE TABLE users (
--     id INT PRIMARY KEY,
--     name VARCHAR(50),
--     email VARCHAR(100),
--     password VARCHAR(100),
--     created_at DATETIME
-- );


-- CREATE TABLE posts (
--     id INT PRIMARY KEY,
--     user_id INT,
--     title VARCHAR(100),
--     content TEXT,
--     created_at DATETIME,
--     FOREIGN KEY (user_id) REFERENCES users(id));


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'comments')
BEGIN
    CREATE TABLE comments (
        id INT PRIMARY KEY,
        post_id INT,
        user_id INT,
        content TEXT,
        created_at DATETIME,
        FOREIGN KEY (post_id) REFERENCES posts(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
END



SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';

-- IF OBJECT_ID('comments', 'U') IS NOT NULL
--     DROP TABLE comments;

-- IF OBJECT_ID('posts', 'U') IS NOT NULL
--     DROP TABLE posts;

-- IF OBJECT_ID('users', 'U') IS NOT NULL
--     DROP TABLE users;


DROP TABLE users, posts CASCADE;
SELECT * FROM sys.tables;

