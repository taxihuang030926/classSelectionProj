CREATE TABLE Courses(
    Course_ID INT primary key,
    Course_Name VARCHAR(40),
    dept VARCHAR(20),
    Course_Description VARCHAR(100),
    Course_Credit INT
);

insert into Courses(Course_ID, Course_Name, dept, Course_Description, Course_Credit) values(1312, "系統程式",  "資訊", "宗杰", 3);
insert into Courses(Course_ID, Course_Name, dept, Course_Description, Course_Credit) values(1314, "機率與統計",  "資訊", "景盛", 3);
insert into Courses(Course_ID, Course_Name, dept, Course_Description, Course_Credit) values(1313, "資料庫系統",  "資訊", "懷中", 3);
insert into Courses(Course_ID, Course_Name, dept, Course_Description, Course_Credit) values(1323, "互聯網路",  "資訊", "宗杰", 3);

select * from Courses;