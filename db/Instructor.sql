CREATE TABLE Instructor(
    I_ID VARCHAR(8) primary key,
    Name varchar(20),
    Department varchar(40)
);

insert into Instructor(I_ID, Name, I_pwd) values("T0000001", "宗杰", "資訊");
insert into Instructor(I_ID, Name, I_pwd) values("T0000002", "景盛", "資訊");
insert into Instructor(I_ID, Name, I_pwd) values("T0000003", "懷中", "資訊");
insert into Instructor(I_ID, Name, I_pwd) values("T0000004", "明機", "資訊");
insert into Instructor(I_ID, Name, I_pwd) values("T0000005", "雅英", "中文");

select * from Instructor;