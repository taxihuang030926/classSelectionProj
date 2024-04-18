CREATE TABLE Courses(
    Course_ID INT primary key,
    Course_Name VARCHAR(40),
    dept VARCHAR(20),
    prereq INT,
    Grade INT,
    Class INT,
    Instructor VARCHAR(100),
    Course_Credit INT
);
/* TODO: 節數 日期 */
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1312, "系統程式", "資訊", 1, 2, 2, "劉宗杰", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1314, "機率與統計", "資訊", 1, 2, 2, "游景盛", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1313, "資料庫系統", "資訊", 1, 2, 2, "許懷中", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1323, "互聯網路", "資訊", 0, NULL, NULL, "劉宗杰", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(2911, "德文（一）", "外語", 0, NULL, NULL, "游曉嵐", 2);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(2984, "音樂行旅 - 巡訪古典音樂大師", "通識", 0, NULL, NULL, "曾韻心", 2);
select * from Courses;