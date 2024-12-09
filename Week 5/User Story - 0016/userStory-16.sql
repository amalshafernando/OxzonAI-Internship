CREATE DATABASE OxzonAi;

USE OxzonAi;

CREATE TABLE Users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(20),
    email VARCHAR(50)
);

INSERT INTO Users(name, email) VALUES
('Raj Kumar', 'rajk@gmail.com'),
('Rahul Kumar', 'rahul@gmail.com'),
('Kareem Uddin', 'k.uddin@gmail.com'),
('Fareed Muhammad', 'm.fareed@gmail.com'),
('Ayesha Khan', 'ayesha.khan@gmail.com'),
('Ali Shah', 'ali.shah@gmail.com'),
('Zara Ali', 'zara.ali@gmail.com'),
('Imran Siddique', 'imran.siddique@gmail.com'),
('Sania Khan', 'sania.khan@gmail.com'),
('Faizan Ahmad', 'faizan.ahmad@gmail.com');


UPDATE Users SET email = 'raj@gmail.com' where id=1;

DELETE FROM Users where id =2;

select * from Users


