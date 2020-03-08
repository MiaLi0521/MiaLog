"""
用来存储扩展实例化等操作
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask_ckeditor import CKEditor

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
ckeditor = CKEditor()


@login_manager.user_loader
def load_user(user_id):
    from mialog.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message = '请先登录'
login_manager.login_message_category = 'warning'
