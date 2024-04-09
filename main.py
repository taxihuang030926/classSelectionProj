#以下是我的程式碼:
from flask import Flask, request,render_template,redirect,session
import os
import MySQLdb

currentlocation = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

def connectServer():
    conn = MySQLdb.connect(host="https://snapshot-medal-fathers-nested.trycloudflare.com/",
                           user="admint",
                           passwd="12341234",
                           db="classselectionproj")
    return conn

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/",methods = ["POST"])
def checklogin():
    UN = request.form.get('Username')
    PW = request.form.get('Password')

    sqlconnection = connectServer()
    curser = sqlconnection.cursor()
    query1 = "SELECT S_ID, S_pwd FROM Student WHERE S_ID = {un} AND S_pwd= {pw})".format(un=UN, pw=PW)

    rows = curser.execute(query1)
    rows = rows.fetchall()
    if len(rows) == 1:
        return redirect
    else:
        return redirect("/")
    
@app.route("/search")
def searchpage():
    return render_template("search.html")

# @myapp.route("/register",methods = ["GET","POST"])
# def registerpage():
#     if request.method == "POST":
#         dUN = request.form['DUsername']
#         dPW = request.form['DPassword']
#         Uemail = request.form['EmalUser']
#         sqlconnection = sqlite3.connect(currentlocation + "\Login.db")
#         curser = sqlconnection.cursor()
#         query1 = "INSERT INTO Users VALUES('{u}','{p}','{e}')".format(u = dUN,d = dPW,e = Uemail)
#         curser.execute(query1)
#         sqlconnection.commit()
#         return redirect("/Login")
#     return render_template("Register.html")

if __name__ == "__main__":
    app.run()



# 請幫我根據圖片以及程式碼找出為什麼執行後網頁會顯示Internal Server Error
# The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
# 的錯誤