from . import auth
from flask import redirect,request, session, flash, render_template, url_for
# from ..models.user import User
from ..extensions import mysql
from app import bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators



class LoginForm(FlaskForm):
    username = StringField("Username",[validators.DataRequired(),validators.Length(min=4,max=100)])
    password = PasswordField("Password",[validators.DataRequired(),validators.Length(min=8)])

class RegisterForm(FlaskForm):
    username = StringField("Username",[validators.DataRequired()])
    password = PasswordField("Password",[validators.DataRequired(),validators.Length(min=8)])
    # confirm = PasswordField("Repeat Password",[validators.DataRequired(),validators.Length(min=8)])
    role = StringField("Role",[validators.DataRequired()])



@auth.route('/login', methods =["GET","POST"])
def login():
    username = ""
    password = ""
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit(): 
        print(form.username.data)      
        cur = mysql.connection.cursor()
        cur.execute("SELECT username, password  FROM users WHERE username = %s", (form.username.data))
        user = cur.fetchone()
        cur.close()
        print(user)
        if not user:
            flash("The username has been taken", "error")
        return render_template('register.html',form=form)

       
    return render_template("login.html",form=form)

@auth.route('/register', methods = ["GET", "POST"])
def register():    
    form = RegisterForm(request.form)
   
    if request.method == "POST" and form.validate_on_submit():          
        cur = mysql.connection.cursor()
        user = cur.execute("SELECT id, username, password  FROM users WHERE username = %s", (form.username.data,))
        username = cur.fetchone()
        cur.close()
        if user:
            flash("The username has been taken", "error")
            return render_template('register.html',form=form)
        else:            
            hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') 
            print(hash_password)
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(username, password,role) VALUES(%s,%s,%s)", (form.username.data,hash_password,form.role.data))
            mysql.connection.commit()
            cur.close()
        
            session['username'] = username
        flash("The user added successfully", "success")
        return render_template('login.html',form=form)
    return render_template('register.html',form=form)


@auth.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("auth.login"))
