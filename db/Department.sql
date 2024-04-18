CREATE TABLE Department(
    Dept_Name varchar(40) primary key,
    Building varchar(20)
);

insert into Department(Dept_Name, Building) values("資訊", "資電");
insert into Department(Dept_Name, Building) values("航太", "工學");
insert into Department(Dept_Name, Building) values("國貿", "商學");
insert into Department(Dept_Name, Building) values("電機", "資電");
insert into Department(Dept_Name, Building) values("中文", "人社");

select * from Department;