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

    if len(result) == 1:
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

    CODE = request.form.get('code')
    DAY = request.form.get('day')
    CNAME = request.form.get('coursename')
    INAME = request.form.get('instructorname')

    query = 'SELECT * FROM course WHERE '

    # print out course table
    if(CODE != ""):
        query += 'course_id="{code}"'.format(code=CODE)

    if(DAY != ""):
        query += 'day="{day}"'.format(day=DAY)
    
    if(CNAME != ""):
        query += 'course_name="%{cname}%"'.format(cname=CNAME)

    if(INAME != ""):
        query += 'instructor_name="%{iname}%"'.format(iname=INAME)
    
    query += ';'
    cursor.execute(query)
    result = cursor.fetchall()
# follow

    # 

    cursor.close()
    return redirect("/search")

# enroll and slot 
@app.route("/enroll")
def enrollmentpage():
    return render_template("enrollment.html")


if __name__ == "__main__":
    app.run(debug=True)
