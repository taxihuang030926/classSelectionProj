from flask import Flask, request, render_template, redirect
import yaml
import mysql.connector as mc
import search, dct_user, dct_pwd

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

sid = ""

# login
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/",methods = ["POST"])
def checklogin():
    cursor = conn.cursor()

    UN = request.form.get('Username')
    PW = request.form.get('Password')
    
    # query1 = 'SELECT * FROM Student'
    query1 = 'SELECT S_ID, S_pwd FROM Student WHERE S_ID="{un}" AND S_pwd="{pw}";'.format(un=UN, pw=PW)
    
    cursor.execute(query1)
    result = cursor.fetchall()
    print(result)

    if len(result) == 1:
        sid = UN
        cursor.close()
        return redirect("/search")
    else:
        cursor.close()
        return redirect ("/")
    

# search
@app.route("/search")
def searchpage(): 
    return render_template("search.html")

@app.route("/search", methods = ["POST"])
def search():
    # methods: code, day, name, instructorname
    # w\ multi select boxes: concatenate the selected values into a string and pass it to the query
    # no select boxes: no need to use the join method
    cursor = conn.cursor()
    SC = request.form.get('Select-Code')
    SD = request.form.get('Select-Day')
    SCN = request.form.get('Select-Coursename')
    SI = request.form.get('Select-Instructorname')
    CODE = request.form.get('Code')
    DAY = request.values.get('Day')
    CNAME = request.form.get('Coursename')
    INAME = request.form.get('Instructorname')
    print(SC, SD, SCN, SI, CODE, DAY, CNAME, INAME)
    flag = 0
    cresult = []
    query = 'SELECT courses.*, Course_Session.Session_Day, Course_Session.Session_RTime, course_session.Classroom,course_session.Session_ID FROM Courses, Course_Session WHERE '
    print("before query")

    # print out course table
    if CODE and SC == "on":
        if not flag:
            print("cond1")
            flag = 1
            query += 'courses.course_id="{code}" AND course_session.course_id="{code}"'.format(code=CODE)
        else:
            print("cond1")
            query += ' AND courses.course_id="{code}" AND course_session.course_id="{code}"'.format(code=CODE)

    if DAY and SD == "on":
        if not flag:
            print("cond2")
            flag = 1
            query += 'course_session.session_day="{day}"'.format(day=DAY)
        else:
            print("cond2")
            query += ' AND course_session.session_day="{day}"'.format(day=DAY)

    if CNAME and SCN == "on":
        if not flag:
            print("cond3")
            flag = 1
            query += 'courses.course_name LIKE "%{cname}%"'.format(cname=CNAME)
        else:
            print("cond3")
            query += ' AND courses.course_name LIKE "%{cname}%"'.format(cname=CNAME)

    if INAME and SI == "on":
        if not flag:
            print("cond4")
            flag = 1
            query += 'courses.instructor LIKE "%{iname}%"'.format(iname=INAME)
        else:
            print("cond4")
            query += ' AND courses.instructor LIKE "%{iname}%"'.format(iname=INAME)

    if not (CODE or DAY or CNAME or INAME):
        query += '""'
    else:
        cursor.execute(query + ' AND Course_Session.Course_ID=Courses.Course_ID ORDER BY Course_Session.Session_ID;')
        cresult = cursor.fetchall()
        query += ' AND Course_Session.Course_ID=Courses.Course_ID AND Course_Session.Session_ID LIKE "%-1%" ORDER BY Course_Session.Session_ID '
    
    query += ';'
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    print("cresult: ")
    print(cresult)
    
    return render_template("search.html", courses=result, cresults=cresult)

# enroll and slot 
@app.route("/enroll")
def enrollmentpage():
    return render_template("enrollment.html")


if __name__ == "__main__":
    app.run(debug=True)
