from . import admin
from flask import render_template, redirect, flash, url_for
from ..extensions import mysql


@admin.route('/reservation')
def reservation():
    cur = mysql.connection.cursor()
    print(cur)
    cur.execute("SELECT guest.id,firstname, lastname,email,phonenumber,address,nationality roomNumber,checkinDate,checkoutDate,paymentStatus,room_type.name " \
    "FROM guest JOIN booking ON guest.id = booking.guestID " \
    "JOIN rooms ON booking.roomID = rooms.id " \
    "JOIN room_type ON rooms.roomTypeID = room_type.id")

    guests = cur.fetchall()
    cur.execute("SELECT id, firstname, lastname from guest")
    selects = cur.fetchall()
    cur.close()
    
    return render_template("reservation.html",guests=guests,selects = selects)
@admin.route('/admin')
def admin():
    return render_template("admin.html")