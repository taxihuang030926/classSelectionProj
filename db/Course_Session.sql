CREATE TABLE Course_Session (
    Session_ID varchar(8) primary key,
    Course_ID INT,
    Session_Day VARCHAR(20),
    Session_RTime INT,
    Session_Time INT,
    Classroom VARCHAR(20),
    Current_Population INT,
    Population_Limit INT,
    foreign key(Course_ID) references Courses(Course_ID),
    foreign key(Classroom) references Classroom(ClassroomName)
);

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1312-1", 1312, "Monday", 3, 3, "資電402", 0, 5);
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1312-2", 1312, "Monday", 4, 4, "資電402", 0, 5);
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1312-3", 1312, "Wednesday", 4, 32, "資電402", 0, 5);

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1314-1", 1314, "Monday", 6, 6, "科航207", 0, 5);
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1314-2", 1314, "Monday", 7, 7, "科航207", 0, 5);
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1314-3", 1314, "Tuesday", 3, 17, "資電504", 0, 5);

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1313-1", 1313, "Monday", 8, 8, "土水304", 0, 5);
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1313-2", 1313, "Monday", 9, 9, "土水304", 0, 5);
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1313-3", 1313, "Tuesday", 4, 18, "資電512", 0, 5);

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1323-1", 1323, "Wednesday", 6, 34, "資電234", 0, 5);
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1323-2", 1323, "Wednesday", 7, 35, "資電234", 0, 5);
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("1323-3", 1323, "Wednesday", 8, 36, "資電234", 0, 5);

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("2911-1", 1323, "Friday", 6, 62, "語文202", 0, 5);
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("2911-2", 1323, "Friday", 7, 63, "語文202", 0, 5);

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("2984-1", 2984, "Wednesday", 6, 34, "人言507", 0, 5);
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom, Current_Population, Population_Limit) values("2984-2", 2984, "Wednesday", 7, 35, "人言507", 0, 5);