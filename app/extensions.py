# from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

# db = SQLAlchemy()
migrate = Migrate()

mysql = MySQL()

bcrypt = Bcrypt()