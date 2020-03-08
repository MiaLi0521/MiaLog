"""
定义用户认证蓝本
"""
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

from mialog import Admin
from mialog.forms import LoginForm
from mialog.utils import redirect_back

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # http://127.0.0.1:5000/ 127.0.0.1:5000 /auth/login /auth/login?name=lmx
    # print(request.host_url, request.host, request.path, request.full_path)
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('欢迎回来!', 'info')
                return redirect_back()
            flash('用户名或密码无效!', 'warning')
        else:
            flash('还没有创建管理员账户!', 'warning')
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('退出成功!', 'info')
    return redirect_back()

