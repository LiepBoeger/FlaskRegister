from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user

home_route_bp = Blueprint('home_route', __name__)

@home_route_bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')
