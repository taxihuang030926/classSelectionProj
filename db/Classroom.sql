CREATE TABLE Classroom(
    ClassroomName varchar(20) primary key,
    Room_Number INT,
    Capacity INT,
    Building varchar(20)
);

insert into Classroom(ClassroomName, Room_Number, Capacity, Building) values("資電234", 234, 5, "資電");
insert into Classroom(ClassroomName, Room_Number, Capacity, Building) values("資電402", 402, 5, "資電");
insert into Classroom(ClassroomName, Room_Number, Capacity, Building) values("資電504", 504, 5, "資電");
insert into Classroom(ClassroomName, Room_Number, Capacity, Building) values("資電512", 512, 5, "資電");
insert into Classroom(ClassroomName, Room_Number, Capacity, Building) values("科航207", 207, 5, "科航");
insert into Classroom(ClassroomName, Room_Number, Capacity, Building) values("土水304", 304, 5, "土水");
insert into Classroom(ClassroomName, Room_Number, Capacity, Building) values("語文202", 202, 5, "語文");
insert into Classroom(ClassroomName, Room_Number, Capacity, Building) values("人言507", 507, 5, "人言");

select * from Classroom;