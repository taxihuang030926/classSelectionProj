create table Student(
    S_ID VARCHAR(8) primary key,
    Name VARCHAR(20),
    Ttl_Credit INT,
    S_pwd VARCHAR(20),
    Dept VARCHAR(20),
    Grade VARCHAR(8),
    Class VARCHAR(8),
);

insert into Student(S_ID, Name, Ttl_Credit, S_pwd, Dept, Grade, Class) values("D1149711", "do-ning", 0, "dooooning666", "資訊", 2, 2);
insert into Student(S_ID, Name, Ttl_Credit, S_pwd, Dept, Grade, Class) values("D1100001", "Std_A", 0, "Std_A", "資訊", 2, 3);
insert into Student(S_ID, Name, Ttl_Credit, S_pwd, Dept, Grade, Class) values("D1100002", "Std_B", 0, "Std_B", "資訊", 1, 2);
insert into Student(S_ID, Name, Ttl_Credit, S_pwd, Dept, Grade, Class) values("D1100003", "Std_C", 0, "Std_C", "資訊", 1, 3);

select * from Student;