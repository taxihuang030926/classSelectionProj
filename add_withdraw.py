from flask import Flask, request, render_template, redirect
from init import student_data, courses_data

def check_schedule(conn, S_ID, CID):
    cursor = conn.cursor()
    C_ID = request.form.get('Class_ID')
    query0 = "SELECT Course_ID FROM Courses;"
    cursor.excute(query0)
    C_ID = cursor.fetchall()
    query1 = "SELECT Session_Time FROM Course_Session WHERE Course_ID={cid};".format(cid=C_ID)
    cursor.execute(query1)
    locations = cursor.fetchall()
    print(locations)

    # for location in locations:
    #     session_time = location[0]  # Assuming Session_Time is the first column
    #     query2 = "SELECT * FROM `Enrolled_Table` WHERE `S_ID`={sid} AND `S{session_time}`;".format(sid=S_ID,)
    #     cursor.execute(query2)
    #     result = cursor.fetchone()

    #     if result is not None:
    #         return True
    
    # return False


def same_course(S_ID, C_ID, connectServer):
    cursor = connectServer.cursor()
    try:
        # 這裡要改
        cursor = connectServer.cursor()
        cursor.execute(f'SELECT * FROM `Enrolled_Table` WHERE `S_ID`={S_ID};')
        schedule = cursor.fetchone()
        for i in schedule:
            cursor.execute(f"SELECT * FROM `Courses` c ON({schedule} = c.Course_ID) WHERE c.course_id = {C_ID};")
            result = cursor.fetchone()
            if result:
                return True
        return False
    finally:
        cursor.fetchall()
        connectServer.commit()
        cursor.close()
    

def add_course(conn, S_ID, C_ID):
    student = student_data(S_ID, conn)
    course = courses_data(C_ID, conn)
    session = session_data(C_ID, conn)

    # 同學只能加選本系的課程
    if student.dept != course.Dept:
        error = '只能加選本系課程'
        return False, error
    
    # 人數已滿的課程不可加選
    elif course.Capacity == course.Cur_ppl:
        error = '人數已滿'
        return False, error
    
    # 不可加選衝堂的課程
    elif check_schedule(S_ID, C_ID):
        error = '衝堂'
        return False, error

    # 不可加選與已選課程同名的課表
    elif same_course(S_ID, C_ID):
        error = '已有同名課程'
        return False, error

    # 加選後學分不可超過最高學分限制 (30 學分)
    elif student.credit + course.Credit > 30:
        error = '已超出學分上限'
        return False, error
    
    return True

# 退選開始
def update_credit(SID, CID, status, connectServer):
    cursor = connectServer.cursor()
    cursor.execute(f'SELECT `Ttl_Credit` FROM `Student` WHERE `S_ID`="{SID}";')
    current_credit = cursor.fetchone()[0]

    cursor.execute(f'SELECT `Course_Credit` FROM `Courses` WHERE `Course_ID`={CID};')
    course_credit = cursor.fetchone()[0]

    if status == 1:
        new_credit = current_credit+course_credit
    else:
        new_credit = current_credit-course_credit

    cursor.execute(f'UPDATE `Student` SET `Ttl_Credit`={new_credit} where `S_ID`={SID};')

    connectServer.commit()
    cursor.close()

def remove_schedule(SID, CID, connectServer):
    cursor = connectServer.cursor()
    schedule = 'schedule_'+SID

    cursor.execute(f'UPDATE `{schedule}` SET `Course_ID`=NULL WHERE `Course_ID`={CID};')
    connectServer.commit()

    # update member
    cursor.execute(f'SELECT `Current_Population` FROM `Course_Session` WHERE `Course_ID`={CID};')
    new_member = int(cursor.fetchone()[0]) - 1
    cursor.execute(f'UPDATE `Course_Session` SET `Current_Population`={new_member} WHERE `Course_ID`={CID};')
    connectServer.commit()

    update_credit(SID, CID, -1, conn)

    cursor.close()

def withdraw(S_ID, Course_ID):
    student = student_data(S_ID)
    course = courses_data(Course_ID)

    # 不可低於最低學分限制
    if student.credit - course.Credit < 9:
        error = '不可低於9學分'
        return False, error
    
    # 退選必修課需提出警告
    elif course.Prereq == 1:
        error = '不可退選必修課'
        return False, error
    
    else:
        remove_schedule(S_ID, Course_ID)
        return True, None