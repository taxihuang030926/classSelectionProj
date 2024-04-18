s_id=""


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
        self.Room_number = Room_number
        self.Capacity = Capacity
        self.Building = Building
        
    def get_Classroom(self):
        return "Room_Number: {}, Capacity: {}, Building: {}".format(self.Room_number, self.Capacity, self.Building)
        


def student(SID, connectServer):

    cur = connectServer.cursor()
    cur.execute("SELECT * FROM student WHERE SID=%s;", (SID,))
    result = cur.fetchone()
    s_id = result[0]
    if result:
        student = Student(S_ID=result[0], Name=result[1], Ttl_Credit=result[2], S_pwd=result[3], dept=result[4])
        cur.close()
        return student, s_id
    else:
        cur.close()
        return None, s_id

def courses(C_ID, connectServer):
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM course WHERE course_id=%s", (C_ID,))
    result = cur.fetchone()
    
    if result:
        course = Courses(Course_ID=result[0], Course_Name=result[1], dept=result[2], Course_Description=result[3], Course_Credit=result[4])
        cur.close()
        return course
    else:
        cur.close()
        return None

def time_slot(connectServer):
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM times_slot")
    results = cur.fetchall()

    times_table_list = []
    for result in results:
        time_entry = Time_slot(TS_ID=result[0], Session=result[1], Course_ID=result[2])
        times_table_list.append(time_entry)

    cur.close()
    return times_table_list


def section(connectServer):
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM Section")
    results = cur.fetchall()
    
    Section_list = []
    for result in results:
        section_entry = Section(Sec_ID=result[0], Semester=result[1], Year=result[2]),
        Section_list.append(section_entry)

    cur.close()
    return Section_list

def instructor(T_ID, connectServer):
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM Instructor WHERE T_ID=%s",(T_ID,))
    result = cur.fetchone()
    
    if result:
        instructor = Instructor(I_ID=result[0], Name=result[1], Dept=result[2])
        cur.close()
        return instructor
    else:
        cur.close()
        return None
    
def department(connectServer):
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM Department")
    results = cur.fetchall()

    department_list = []
    for result in results:
        department = Department(Dept_Name=result[0], Building=result[1])
        department_list.append(department)

    cur.close()
    return department_list


def classroom(connectServer):
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM Classroom")
    results = cur.fetchall()
    print(results)

    classroom_list = []
    for result in results:
        classroom = Classroom(result[0], result[1], result[2])
        print(classroom.get_Classroom())
        classroom_list.append(classroom)

    cur.close()
    return classroom_list