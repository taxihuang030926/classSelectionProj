from flask import Flask, request,render_template,redirect,session
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

# testcursor = conn.cursor()
# testcursor.execute("SELECT * FROM Student")
# result = testcursor.fetchall()
# for i in result:
#     print(i)

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

        return redirect("/search")
    else:
        return redirect ("/")
    
# search
@app.route("/search")
def searchpage():
    return render_template("search.html")

    # print out course table

    # follow

    # 

# enroll and slot 
@app.route("/enrollment")
def enrollmentpage():
    return render_template("enrollment.html")


if __name__ == "__main__":
    app.run(debug=True)
