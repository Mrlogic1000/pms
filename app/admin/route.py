from . import admin
from flask import render_template, redirect, flash, url_for
from ..extensions import mysql


@admin.route('/pms')
def pms():
    cur = mysql.connection.cursor()
    cur.execute("SELECT guest.id,lastname,firstname,email,phonenumber,address,nationality,checkinDate,checkoutDate,paymentStatus FROM guest,booking WHERE guest.id = booking.guestID")
    guests = cur.fetchall()
    cur.close()
    for guest in guests:
        print(guest)
    
    return render_template("pms.html",guests=guests)