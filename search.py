import mysql.connector
from flask import Flask, request, render_template
from connect_db import connectServer
import init  

app = Flask(__name__)

# 假設你已經有一個初始化資料庫連接的函數如下
connectServer = init.connect_db()

def search_query(time, weekday, course_code, teacher, department):
    cur = connectServer.cursor()

    # 初始化 SQL 查詢字串和參數列表
    query = "SELECT * FROM your_table_name WHERE 1=1"
    params = []

    # 根據使用者提交的條件組合 SQL 查詢
    if time:
        query += " AND time_column = %s"
        params.append(time)
    if weekday:
        query += " AND weekday_column = %s"
        params.append(weekday)
    if course_code:
        query += " AND course_code_column = %s"
        params.append(course_code)
    if teacher:
        query += " AND teacher_column = %s"
        params.append(teacher)
    if department:
        query += " AND department_column = %s"
        params.append(department)

    cur.execute(query, params)
    results = cur.fetchall()

    cur.close()
    return results

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        time = request.form.get("time")
        weekday = request.form.get("weekday")
        course_code = request.form.get("course_code")
        teacher = request.form.get("teacher")
        department = request.form.get("department")
        
        results = search_query(time, weekday, course_code, teacher, department)
        
        # 傳遞查詢結果到前端
        return render_template("search_results.html", results=results)
    
    return render_template("search_form.html")

# if __name__ == "__main__":
#     app.run(debug=True)
