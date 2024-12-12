from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64


# Blueprintの作成
article_bp = Blueprint('article', __name__, url_prefix='/graph')


@article_bp.route('/enn')
def enn():
    
    count_tag_list = [10, 20, 30, 40, 50]
    
    labels = ['Python', 'Ruby', 'Java', 'PHP', 'JavaScript']
    plt.pie(count_tag_list, labels=labels, autopct='%.f%%', labeldistance=None)
    plt.legend()
    plt.title('Language')
    
    buf = BytesIO()
    plt.savefig(buf, format="png")
    
    #画像データをBase64にエンコード
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    #エンコードしたデータをHTMLに渡す
    return render_template('graph.html', data=data)


@article_bp.route('/bou',)
def bou():


    
    return render_template('graph.html')
