CREATE TABLE Classroom(
    Room_Number INT primary key,
    Capacity INT,
    Building varchar(20)
);

insert into Classroom(Room_Number, Capacity, Building) values(234, 5, "資電");
insert into Classroom(Room_Number, Capacity, Building) values(402, 5, "資電");
insert into Classroom(Room_Number, Capacity, Building) values(512, 5, "資電");
insert into Classroom(Room_Number, Capacity, Building) values(1234, 5, "科航");

select * from Classroom;