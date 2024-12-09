SELECT SYSTEM_USER;

SELECT name 
FROM sys.syslogins 
WHERE is_disabled = 0;


SELECT SUSER_NAME();


select @@ServerName