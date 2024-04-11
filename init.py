class Student:
    def __init__(self, S_ID, Name, Ttl_Credit, S_pwd, dept):
        self.sid = S_ID
        self.name = Name
        self.credit = Ttl_Credit
        self.password = S_pwd
        self.dept = dept
                
    def get_student_data(self):
        return " SID: {}, Name :{}, Total Credit: {}, Dept: {}".format(self.sid, self.name, self.credit, self.dept)
    

class Courses:
    def __init__(self, Course_ID, Course_Name, Course_Dept, Course_Description, Course_Credit):
        self.ID = Course_ID
        self.Name = Course_Name
        self.Dept = Course_Dept
        self.Description = Course_Description
        self.Credit = Course_Credit
        
    def get_class_data(self):
        return " Class_ID: {}, Class_Name :{}, Dept: {}, Desc: {}, Credit".format(self.ID, self.Name, self.dept, self.Description, self.Credit)
 
class Time_slot:
    def __init__(self, TS_ID, Session, Course_ID):
        self.TS_ID = TS_ID
        self.Session = Session
        self.CourseID = Course_ID
        
    def get_time_slot(self):
        return "TS_ID: {}, Session: {}, Course_ID: {}".format(self.TS_ID, self.Session, self.CourseID)
    
class Section:
    def __init__(self, SEC_ID, Semester, Year):
        self.SecID = SEC_ID
        self.Semester = Semester
        self.Year = Year
        
    def get_Section(self):
        return "SEC_ID: {}, Semester: {}, Year: {}".format(self.SecID, self.Semester, self.Year)
    
class Instructor:
    def __init__(self, I_ID, Name, dept):
        self.Inst_ID = I_ID
        self.Name = Name
        self.dept = dept
        
    def get_Instructor(self):
        return "Instructor_ID: {}, Name: {}, Instructor_dept: {}".format(self.Inst_ID, self.Name, self.dept)
    
class Department:
    def __init__(self, Dept_Name, Building):
        self.DeptName = Dept_Name
        self.Building = Building
        
    def get_dept(self):
        return "Dept_Name: {}, Building: {}".format(self.DeptName, self.Building)
    
class Classroom:
    def __init__(self, Room_number, Capacity, Building):
        self.RoomNumber = Room_number
        self.Capacity = Capacity
        self.Building = Building
        
    def get_Classroom(self):
        return "Room_Number: {}, Capacity: {}, Building: {}".format(self.RoomNumber, self.Capacity, self.Building)
        

    