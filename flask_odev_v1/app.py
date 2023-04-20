from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from session_interface import mySessionInterface
from validate_user import validate_member,add_member


app = Flask(__name__)
app.secret_key = "super secret key"
app.session_interface = mySessionInterface()
app.secret_key = "super secret key"

member_login = None
login_status = False

@app.route('/')
def index():
    return render_template('index.html',member_login = member_login)

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        print("post")
        username = request.form['username']
        print(username)
        email = request.form['email']
        password = request.form['password']
        print('before')
        add_member(username,email,password)
        return render_template('login')
    return render_template('signup.html')


@app.route('/login',methods =['GET','POST'])
def login():

    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        member_login = validate_member(username,password)
        login_status = True
        return render_template('index.html',member_login =member_login,login_status=login_status)
    
    return render_template('login.html')



@app.route('/logout')
def logout():
    return render_template('index.html',member_login=member_login,login_status=login_status)

@app.route('/about')
def about():
    return render_template('about.html',member_login=member_login,login_status=login_status)


if __name__ == "__main__":
    app.run(debug=True)
