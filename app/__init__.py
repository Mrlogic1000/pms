from flask import Flask, render_template, request, session, redirect, url_for, flash
from .extensions import mysql,migrate, bcrypt,Environment,Bundle
from dotenv import load_dotenv

from os import environ

load_dotenv()

def get_settings():
    return environ.get('SETTINGS')


def create_app():

    app = Flask(__name__)

    app.config.from_object(get_settings())   
    # assets = Environment(app)
    # assets.url = app.static_url_path
    # scss = Bundle('scss/admin.scss',  filters='libsass', output='css/admin.css')
    # assets.register('admin_css', scss)
    
    
    # db.init_app(app)
    mysql.init_app(app)
    bcrypt.init_app(app)
    # migrate.init_app(app,db)
    
    
    

    # from . import models
    from .auth import auth
    from .home import home
    from .admin import admin

    
    app.register_blueprint(admin, url_prefix="/" )
    app.register_blueprint(home, url_prefix="/" )
    app.register_blueprint(auth, url_prefix="/")
    # app.register_blueprint(api, url_prefix='/api' )

   


    return app