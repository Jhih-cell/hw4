
from flask import Flask, session, redirect, url_for, request, render_template
from markupsafe import escape
app=Flask(__name__,
          static_folder="public",
          static_url_path="/"
)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#首頁路由
@app.route("/")
def index():    
    return render_template("index.html")

#驗證功能的路由
@app.route("/signin" ,methods=["POST"])
def signin():
    id=request.form["ID"]
    password=request.form["password"]
    if id == "test" and password == "test":
        #驗證成功後，在後端 Session 中記錄使用者狀態為已登入
        session['username']=request.form['ID']
        #並導向成功登入路由
        return redirect("/member/")
    else:
        #驗證失敗，將使用者導向到【失敗頁面網址】
        return redirect("/error/")
        
#成功登入的路由
@app.route("/member/" )
def member():
    #檢查使用者狀態
    if 'username' in session:
        #驗證成功，將使用者導向到【成功頁面網址】
        return render_template("member.html")
    #在後端Session 中記錄使用者狀態為未登入，並導向【首頁】
    return redirect("/")
#驗證失敗的路由
@app.route("/error/")
def error():    
    return render_template("error.html")
#登出狀態的路由
@app.route('/signout')
def logout():
    #連線到【登出功能網址】，在後端Session 中記錄使用者狀態為未登入
    session.pop('username', None)
    #並導向【首頁】
    return redirect('/')


app.run(port=3000)