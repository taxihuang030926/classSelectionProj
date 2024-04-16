CREATE TABLE Courses(
    Course_ID INT primary key,
    Course_Name VARCHAR(40),
    dept VARCHAR(20),
    Course_Description VARCHAR(100),
    Course_Credit INT, 
    Category VARCHAR(20)
);

insert into Courses(Course_ID, Course_Name, dept, Course_Description, Course_Credit, Category) values(1312, "系統程式",  "資訊", "宗杰", 3, "必修");
insert into Courses(Course_ID, Course_Name, dept, Course_Description, Course_Credit, Category) values(1314, "機率與統計",  "資訊", "景盛", 3, "必修");
insert into Courses(Course_ID, Course_Name, dept, Course_Description, Course_Credit, Category) values(1313, "資料庫系統",  "資訊", "懷中", 3, "必修");
insert into Courses(Course_ID, Course_Name, dept, Course_Description, Course_Credit, Category) values(1323, "互聯網路",  "資訊", "宗杰", 3, "選修");

select * from Courses;
