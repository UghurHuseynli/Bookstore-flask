from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, template_folder='./Templates', static_folder='./static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:windwalker@127.0.0.1:3306/Bookshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'windwalker_key'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Bu sehifeni görmək üçün hesabınıza giriş edin"
db = SQLAlchemy(app)
from url import *



migrate = Migrate(app, db, compare_type=True)
from models import *



if __name__ == '__main__':
    app.run(debug=True)
