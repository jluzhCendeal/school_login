from app.main import main
from flask import render_template, request

from app.models.user import User


@main.route('/admin_login')
def login():
    user = User.query.filter_by(name=request.values.get('user')).first()
    if user is not None and user.comfirm_password(request.values.get('password')):
        return 'login'
    return render_template('admin_login.html')


@main.route('/admin_home')
def home():
    return render_template('home.html')


@main.route('/admin_update_date')
def update_date():
    pass


@main.route('/admin_schooldays')
def schooldays():
    pass


@main.route('/admin_create_schooldays')
def create_schooldays():
    pass


@main.route('/admin_modify_schooldays')
def modify_schooldays():
    pass


@main.route('/admin_del_schooldays')
def del_schooldays():
    pass
