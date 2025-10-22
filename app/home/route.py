from flask import render_template
from ..extensions import mysql

from . import home

@home.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()

    return render_template("home.html", users = users)