from flask import Flask, request, render_template, redirect
from init import student_data, courses_data, time_slot_data, enrolledtable_data


def check_schedule(S_ID, 幾堂課):
    schedule_name = 'schedlue_'+S_ID
    schedule = enrolledtable_data(schedule_name)
    
    for i in range(S幾, 幾堂課):
        if schedule[i] != None:
            return False
    return True

def add_course(S_ID, Courses_ID):
    student = student_data(S_ID)
    course = courses_data(Courses_ID)
    #判斷學分是否超過上限
    if course.Credit + student.Ttl_Credit >= 30:
        wrong = '學分達上限'
        return False, wrong
    #判斷是否為本系課程
    elif course.Dept != student.dept and course.Dept != None:
        wrong = '不可以選其他系的課程'
        return False, wrong
        
    #判斷人數是否已滿
    elif 目前加選人數 == Classroom.Capacity:
        wrong = '人數已滿'
        return False, wrong
        
    #判斷是否衝堂
    elif not check_schedule:
        wrong = '衝堂了bitch'
        return False, wrong
    #判斷課程是否同名

@app.route("/")
def withdraw(): #退選
    return

@app.route("/")
def homepage():
    return render_template("index.html")
