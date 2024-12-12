from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

# Blueprintの作成
article_bp = Blueprint('article', __name__, url_prefix='/graph')


@article_bp.route('/enn')
def enn():
    

    return render_template('graph.html')


@article_bp.route('/bou',)
def bou():


    
    return render_template('graph.html')
