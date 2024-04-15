CREATE TABLE EnrolledTable{
    S_ID VARCHAR(8),
    C_ID VARCHAR(8),
    Grade INT,
    primary key(S_ID, C_ID),
    foreign key(S_ID) references Student(S_ID),
    foreign key(C_ID) references Course(C_ID)
}