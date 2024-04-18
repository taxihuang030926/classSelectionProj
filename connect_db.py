import mysql.connector
import yaml, os
from flask import Flask, request, render_template, redirect
import init

currentlocation = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

def load(filename="config.yml"):
    with open(filename, "r", encoding="utf-8") as config_file:
        return yaml.load(config_file, Loader=yaml.Loader)

import_data = load()
#建立資料庫連線
connectServer = mysql.connector.connect(
    host=import_data.get('database',{}).get('host',''),
    port=import_data.get('database',{}).get('port',''),
    user=import_data.get('database',{}).get('user',''),
    password=import_data.get('database',{}).get('password',''),
    database=import_data.get('database',{}).get('database',''),
)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/",methods = ["POST"])
def checklogin():
    UN = request.form.get('Username')
    PW = request.form.get('Password')

    curser = connectServer.cursor()
    query1 = 'SELECT S_ID, S_pwd FROM Student WHERE S_ID = "{un}" AND S_pwd= "{pw}";'.format(un=UN, pw=PW)

    curser.execute(query1) #建立一個 游標對象
    rows = curser.fetchall()
    if len(rows) == 1:
        return redirect
    else:
        return redirect("/")
    
@app.route("/search")
def searchpage():
    return render_template("search.html")


def student(SID):
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM student WHERE SID=%s;", (SID,))
    result = cur.fetchone()
    
    if result:
        student = init.Student(S_ID=result[0], Name=result[1], Ttl_Credit=result[2], S_pwd=result[3], dept=result[4])
        cur.close()
        return student
    else:
        cur.close()
        return None

def courses(C_ID):
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM course WHERE course_id=%s", (C_ID,))
    result = cur.fetchone()
    
    if result:
        course = init.Courses(Course_ID=result[0], Course_Name=result[1], dept=result[2], Course_Description=result[3], Course_Credit=result[4])
        cur.close()
        return course
    else:
        cur.close()
        return None

def time_slot():
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM times_slot")
    results = cur.fetchall()

    times_table_list = []
    for result in results:
        time_entry = init.Time_slot(TS_ID=result[0], Session=result[1], Course_ID=result[2])
        times_table_list.append(time_entry)

    cur.close()
    return times_table_list


def section():
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM Section")
    results = cur.fetchall()
   
    Section_list = []
    for result in results:
       section_entry = init.Section(Sec_ID=result[0], Semester=result[1], Year=result[2]),
       Section_list.append(section_entry)
       
    cur.close()
    return Section_list
       
   
def instructor(T_ID):
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM Instructor WHERE T_ID=%s",(T_ID,))
    result = cur.fetchone()
    
    if result:
        instructor = init.Instructor(I_ID=result[0], Name=result[1], Dept=result[2])
        cur.close()
        return instructor
    else:
        cur.close()
        return None
    
def department():
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM Department")
    results = cur.fetchall()

    department_list = []
    for result in results:
        department = init.Department(Dept_Name=result[0], Building=result[1])
        department_list.append(department)

    cur.close()
    return department_list


def classroom():
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM Classroom")
    results = cur.fetchall()

    classroom_list = []
    for result in results:
        # 假设 Classroom 类是用来表示教室的类
        classroom = init.Classroom(Room_Number=result[0], Capacity=result[1], Building=result[2])
        classroom_list.append(classroom)

    cur.close()
    return classroom_list



if __name__ == "__main__":
    app.run(debug=True)