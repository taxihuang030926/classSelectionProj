from flask import Flask, request, render_template, redirect
import yaml
import mysql.connector as mc
import init, Search #, Enrollment

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
    print(f"login: {result}\n")

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
    return Search.osearch(conn)

# enroll, withdraw and slot 
@app.route("/search", methods = ["POST"])
def enrollment():
    
    # return Enrollment.oenroll(conn)
    return render_template("search.html")

@app.route("/search", methods = ["POST"])
def slot():
    return render_template("search.html")

@app.route("/enrolledtable")
def enrolltable():
    return render_template("enrolledtable.html")

if __name__ == "__main__":
    app.run(debug=True)

