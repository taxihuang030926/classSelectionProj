from flask import Flask, request, render_template, redirect, url_for
import yaml
import mysql.connector as mc
from Search import osearch
from enrolled_table import getschedlue
from init import student_data

UN = ""

def load(filename="config.yml"):
    with open(filename, "r", encoding="utf-8") as config_file:
        return yaml.load(config_file, Loader=yaml.Loader)

import_data = load()

app = Flask(__name__)

conn = mc.connect(host=import_data.get('database', {}).get('host', ''),
                  port=import_data.get('database', {}).get('port', ''),
                  user=import_data.get('database', {}).get('user', ''),
                  passwd=import_data.get('database', {}).get('password', ''),
                  database=import_data.get('database', {}).get('database', ''))

# login
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def checklogin():
    global UN
    cursor = conn.cursor()

    UN = request.form.get('Username')
    PW = request.form.get('Password')
    
    student = student_data(UN, conn)
    
    query1 = 'SELECT S_ID, S_pwd FROM Student WHERE S_ID=%s AND S_pwd=%s;'
    
    cursor.execute(query1, (UN, PW))
    result = cursor.fetchall()
    print(f"login: {result}\n")
    
    schedule_data = getschedlue(conn, UN)
    
    cursor.close()

    if len(result) == 1:
        return redirect(url_for('searchpage', student=student, schedule_data=schedule_data))
    else:
        return redirect("/")

# search
@app.route('/search', methods=['GET', 'POST'])
def searchpage():
    student = student_data(UN, conn)
    result, cresult = osearch(conn)
    schedule_data = getschedlue(conn, UN)
    
    return render_template("search.html", student=student, schedule_data=schedule_data, courses=result, cresults=cresult)

@app.route("/enrolledtable")
def enrolltable():
    student = student_data(UN, conn)
    schedule_data = getschedlue(conn, UN)
    return render_template("enrolledtable.html", student=student, schedule_data=schedule_data)

if __name__ == "__main__":
    app.run(debug=True)
