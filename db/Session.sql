CREATE TABLE Session {
    Session_ID varchar(8) primary key,
    Course_ID INT,
    Day VARCHAR(20),
    Start_Session INT,
    Duration INT,
    Classroom VARCHAR(20),
    foreign key(Course_ID) references Courses(Course_ID),
    foreign key(S_ID) references Student(S_ID)
}

insert into Session(Session_ID, Course_ID, Day, Start_Session, Duration, Room) values("1312-1", 1312, "Monday", 3, 2, "資電402");
insert into Session(Session_ID, Course_ID, Day, Start_Session, Duration, Room) values("1312-2", 1312, "Wednesday", 32, 1, "資電402");

insert into Session(Session_ID, Course_ID, Day, Start_Session, Duration, Room) values("1314-1", 1314, "Monday", 6, 2, "科航402");
insert into Session(Session_ID, Course_ID, Day, Start_Session, Duration, Room) values("1314-2", 1314, "Tuesday", 18, 1, "資電504");

insert into Session(Session_ID, Course_ID, Day, Start_Session, Duration, Room) values("1313-1", 1313, "Monday", 8, 2, "土水304");
insert into Session(Session_ID, Course_ID, Day, Start_Session, Duration, Room) values("1313-2", 1313, "Tuesday", 17, 1, "資電512");

insert into Session(Session_ID, Course_ID, Day, Start_Session, Duration, Room) values("1323-1", 1323, "Wednesday", 34, 3, "資電234");