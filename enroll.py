import mysql.connector
import yaml, os
from flask import Flask, request, render_template, redirect
from init import Students
from init import Courses

currentlocation = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route("/enroll", methods = ["POST"]) #定義路由，後面所接的是一個要執行的function
def enroll(): #加選
    Course_Name = request.form.get('coursename')
    dept = request.form.get('dept')
    
    sqlconnection = connectServer() #建立連接
    curser = sqlconnection.cursor() #創建游標
    
    rows = curser.execute(query1)
    
    rows = rows.fetchall()
    
    query1 = "SELECT Ttl_Credit FROM Student WHERE S_ID = Username"
    query2 = "SELECT Course_Name, dept FROM Courses WHERE Course_Name = {cn} AND dept = {d};".format(cn=Course_Name, d=dept)
    query3 = "SELECT Session FROM Time_Slot"
    query4 = "SELECT Course_Name FROM Courses"
    query5 = "SELECT Capacity FROM Classroom"
    
    # if +course_credit (=Ttl_Credit) < 能選的學分數
        # if course_dept = student_dept: 科系
            # if time_slot_session = NULL 衝堂
                # if course_name != course_name 同名課程
                    # if now_capacity < capacity: 容納人數
                        #加進去
                    # else
                        # 關注 加進陣列
                # else 不可以加
            # else 不可以加
        # else 不可以加
    # else 不可以加
    
    
    #判斷學分是否超過上限
    if Courses.Course_Credit + Student.Ttl_Credit >= 30:
        wrong = '學分達上限'
        return False, wrong
    
    #判斷是否為本系課程
    elif Courses.dept != Student.dept and Courses.dept != None:
        wrong = '不可以選其他系的課程'
        return False, wrong
    
    #判斷人數是否已滿
    elif 目前加選人數 == Classroom.Capacity:
        wrong = '人數已滿'
        return False, wrong
    
    #判斷是否衝堂
    elif check_schedule ():
        wrong = '衝堂'
        return False, wrong
    
    #判斷課程是否同名
    elif same_course:
        wrong = '已有同名的課程'
        return False, wrong

@app.route("/")
def homepage():
    return render_template("index.html")