--USE master;
-- GO
-- Disconnect all users and rollback active transactions
-- ALTER DATABASE [Demo] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
-- GO
-- Drop the database
--DROP DATABASE [Demo];
--GO

-- simplest
SELECT name FROM sys.databases
ORDER BY name;