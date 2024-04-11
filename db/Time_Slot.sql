CREATE TABLE Time_Slot(
    TS_ID varchar(10) primary key,
    Session varchar(10),
    Course_ID INT,
    FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID)
);

insert into Time_Slot(TS_ID, Session, Course_ID) values("1312-3", 3, 1312);
insert into Time_Slot(TS_ID, Session, Course_ID) values("1312-4", 4, 1312);

insert into Time_Slot(TS_ID, Session, Course_ID) values("1314-6", 6, 1314);
insert into Time_Slot(TS_ID, Session, Course_ID) values("1314-7", 7, 1314);

insert into Time_Slot(TS_ID, Session, Course_ID) values("1313-8", 8, 1313);
insert into Time_Slot(TS_ID, Session, Course_ID) values("1313-9", 9, 1313);

insert into Time_Slot(TS_ID, Session, Course_ID) values("1323-34", 34, 1323);
insert into Time_Slot(TS_ID, Session, Course_ID) values("1323-35", 35, 1323);
insert into Time_Slot(TS_ID, Session, Course_ID) values("1323-36", 36, 1323);


select * from Time_Slot;