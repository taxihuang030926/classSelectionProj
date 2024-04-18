import mysql.connector
import yaml, os
from flask import Flask, request, render_template, redirect
import init 
import add_withdraw

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
    query1 = 'SELECT * FROM Student WHERE S_ID = "{un}" AND S_pwd= "{pw}";'.format(un=UN, pw=PW)

    curser.execute(query1) #建立一個 游標對象
    rows = curser.fetchall()
    
    if len(rows) == 1:
        global student_data 
        init.s_id = UN
        student_data = init.Student(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4])
        excalibur = student_data.get_student_data()
        
        # print(excalibur)
        return redirect("/search") 
    else:
        return redirect
    
@app.route("/search")
def searchpage():
    add_withdraw.hoho()
    print("test: ")
    for i in init.classroom(connectServer):
        print((str)(i.Building)+(str)(i.Room_number))
        
    print(student_data.get_student_data())
    return render_template("/search.html",student=student_data.name)

def time_slot():
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM times_slot")
    results = cur.fetchall()


print()

if __name__ == "__main__":
    app.run(debug=True)

