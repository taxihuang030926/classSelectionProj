CREATE TABLE Students (
    S_ID int PRIMARY KEY AUTO_INCREMENT,
    Name varchar(75) NOT NULL,
    Total_Credit int NOT NULL,
    Password varchar(75) NOT NULL,
);

CREATE TABLE Instructor (
    I_ID int PRIMARY KEY AUTO_INCREMENT,
    Name varchar(75) NOT NULL,
    Password varchar(75) NOT NULL,
);

