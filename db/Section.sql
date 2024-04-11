CREATE TABLE Section(
    Sec_ID varchar(10) primary key,
    Semester INT,
    Year INT
);

insert into Section(Sec_ID, Semester, Year) values("112-1", 1, 112);
insert into Section(Sec_ID, Semester, Year) values("112-2", 2, 112);
insert into Section(Sec_ID, Semester, Year) values("113-1", 1, 113);
insert into Section(Sec_ID, Semester, Year) values("113-2", 2, 113);

select * from Section;