CREATE TABLE Instructor(
    I_ID VARCHAR(8) primary key,
    Name varchar(20),
    I_pwd varchar(20)
);

insert into Instructor(I_ID, Name, I_pwd) values("T0000001", "宗杰", "1");
insert into Instructor(I_ID, Name, I_pwd) values("T0000002", "景盛", "2");
insert into Instructor(I_ID, Name, I_pwd) values("T0000003", "懷中", "3");
insert into Instructor(I_ID, Name, I_pwd) values("T0000004", "明機", "4");
insert into Instructor(I_ID, Name, I_pwd) values("T0000005", "雅英", "5");

select * from Instructor;