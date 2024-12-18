from flask import Blueprint, render_template, request, redirect, url_for # type: ignore
from datetime import datetime
from models import Article, Tag, User
import sqlite3
import collections
import numpy as np
import matplotlib.pyplot as plt
import base64
from matplotlib.figure import Figure
from io import BytesIO

# Blueprintの作成
graph_bp = Blueprint('graph', __name__, url_prefix='/graph')

@graph_bp.route('/')
def list():
    # 円グラフの画像を取得
    ennData = enn()

    
    # 棒グラフの画像を取得
    bouData = bou()

    #エンコードしたデータをHTMLに渡す
    return render_template('graph.html',ennData=ennData,bouData=bouData)


def enn():
    tag = Tag.select()  
    
    # tagそれぞれの記事数を取得
    Pyhon = Article.select().where(Article.tag == 1).count()
    Ruby = Article.select().where(Article.tag == 2).count()
    Java = Article.select().where(Article.tag == 3).count()
    PHP = Article.select().where(Article.tag == 4).count()
    JavaScript = Article.select().where(Article.tag == 5).count()
    
    
    tag = [Pyhon, Ruby, Java, PHP, JavaScript]
    labels = ['Python', 'Ruby', 'Java', 'PHP', 'JavaScript']
    
    # グラフ描画
    fig = Figure()
    ax = fig.subplots()
    ax.pie(tag, labels=labels, autopct='%.f%%', labeldistance=None)
    ax.legend()
    ax.set_title('Language')

    # 画像をバッファに保存
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)  # バッファのポインタを先頭に戻す
    
    # 画像データをBase64にエンコード
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    buf.close()  # バッファを閉じる
    
    # エンコードしたデータを返す
    return data
    
    

def bou():
    user = User.select
    user1 = User.select().where(User.age >= 10).count()
    user10 = User.select().where(User.age >= 10, User.age < 20).count()
    user20 = User.select().where(User.age >= 20, User.age < 30).count()
    user30 = User.select().where(User.age >= 30, User.age < 40).count()
    user40 = User.select().where(User.age >= 40, User.age < 50).count()
    user50 = User.select().where(User.age >= 50, User.age < 60).count()
    user60 = User.select().where(User.age >= 60, User.age < 70).count()
    user70 = User.select().where(User.age >= 70, User.age < 80).count()
    user80 = User.select().where(User.age >= 80, User.age < 90).count()
    user90 = User.select().where(User.age >= 90, User.age < 100).count()
    user100 = User.select().where(User.age >= 100, User.age < 10000000).count()
   
    user = [user1, user10, user20, user30, user40, user50, user60, user70, user80, user90, user100]
    label = ['10歳未満', '10代', '20代', '30代', '40代', '50代', '60代', '70代', '80代', '90代', '100歳以上']
    width = 0.35

    
    # グラフ描画
    fig = Figure()
    ax = fig.subplots()
    ax.bar(label, user, width)
    
    # 画像をバッファに保存
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)  # バッファのポインタを先頭に戻す
    
    # 画像データをBase64にエンコード
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    buf.close()  # バッファを閉じる
    
    # dataを出力
    print("BouData:"+data)

#エンコードしたデータを返す
    return  data
