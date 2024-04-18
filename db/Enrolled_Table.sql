CREATE TABLE EnrolledTable{
    S_ID VARCHAR(8),
    Course_ID INT,
    Grade INT,
    primary key(S_ID, C_ID),
    foreign key(S_ID) references Student(S_ID),
    foreign key(Course_ID) references Courses(Course_ID)
}