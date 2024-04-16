create table Student(
    S_ID VARCHAR(8) primary key,
    Name VARCHAR(20),
    Ttl_Credit INT,
    S_pwd VARCHAR(20),
    dept VARCHAR(20),
    grade VARCHAR(20)
);

insert into Student(S_ID, Name, Ttl_Credit, S_pwd, dept, grade) values("D1149711", "do-ning", 0, "dooooning666", "資訊", "二乙");
insert into Student(S_ID, Name, Ttl_Credit, S_pwd, dept, grade) values("D1100001", "Std_A", 0, "Std_A", "資訊", "二乙");
insert into Student(S_ID, Name, Ttl_Credit, S_pwd, dept, grade) values("D1100002", "Std_B", 0, "Std_B", "資訊", "二乙");
insert into Student(S_ID, Name, Ttl_Credit, S_pwd, dept, grade) values("D1100003", "Std_C", 0, "Std_C", "資訊", "二甲");
insert into Student(S_ID, Name, Ttl_Credit, S_pwd, dept, grade) values("D1100004", "Std_D", 0, "Std_D", "電機", "二甲");

select * from Student;
