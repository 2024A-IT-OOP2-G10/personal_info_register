from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from models import User

# Blueprintの作成
article_bp = Blueprint('article', __name__, url_prefix='/graph')


@article_bp.route('/enn')
def enn():
    

    return render_template('graph.html')


@article_bp.route('/bou',)
def bou():
    user = User.select
    user1 = User.select().where(User.age >= 10).count()
    user10 = User.select().where(User.age >= 10, User.age < 20).count()
    user20 = User.select().where(User.age >= 20, User.age < 30).count()
    user = [user1, user10, user20]
    label = ['10歳未満', '10代', '20代', '30代', '40代', '50代', '60代', '70代', '80代', '90代', '100歳以上']

    
    return render_template('graph.html')
