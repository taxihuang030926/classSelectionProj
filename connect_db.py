import mysql.connector
import yaml
from init import Student, Courses

def load(filename="config.yml"):
    with open(filename, "r", encoding="utf-8") as config_file:
        return yaml.load(config_file, Loader=yaml.Loader)

import_data = load()
#建立資料庫連線
connect = mysql.connector.connect(
    host=import_data.get('database',{}).get('host',''),
    port=import_data.get('database',{}).get('port',''),
    user=import_data.get('database',{}).get('user',''),
    password=import_data.get('database',{}).get('password',''),
    database=import_data.get('database',{}).get('database',''),
)

# 想查詢的 query 指令
# query = "SELECT * FROM people WHERE ... '{}%'.".format(my_head)

# 執行查詢
# cur = connect.cursor()
# cur.execute() #資料上傳位置
# results = "1";

def student_data(SID):
    cur = connect.cursor()
    cur.execute("SELCT * FROM student WHERE SID=%s;", (SID,))
    result = cur.fetchone()
    
    
    if result:
        student = Student(S_ID=result[0], Name=result[1], Ttl_Credit=result[2], dept=result[3])
        cur.close()
        return student
    else:
        cur.close()
        return None

def course_data(course_id):
    cur = connect.cursor()
    cur.execute("SELECT * FROM course WHERE course_id=%s", (course_id,))
    result = cur.fetchone()
    
    if result:
        course = Courses(Course_ID=result[0], Course_Name=result[1], Course_Description=result[2], Course_Credit=result[3])
        cur.close()
        return course
    else:
        cur.close()
        return None


# # 取得並列出所有查詢結果
#     for (description, ) in cur.fetchall():
#         results += "<p>{}</p>".format(description)
#     return results