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
    def __init__(self, Course_ID, Course_Name, Course_Description, Course_Credit):
        self.ID = Course_ID
        self.Name = Course_Name
        self.Desc = Course_Description
        self.Credit = Course_Credit
        
    def get_class_data(self):
        return " Class_ID: {}, Class_Name :{}, Credit: {}, Desc: {}".format(self.ID, self.Name, self.Credit, self.Desc)