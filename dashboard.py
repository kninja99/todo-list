from flask import Blueprint, render_template, redirect

user_dashboard = Blueprint('user_dashboard', __name__,
                           static_folder='static', template_folder='templates')


@user_dashboard.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
