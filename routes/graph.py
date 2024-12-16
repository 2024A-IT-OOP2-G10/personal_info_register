from flask import Blueprint, render_template, request, redirect, url_for # type: ignore
from datetime import datetime
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
    
    # 棒グラフの画像を取得
    bouData = bou()
    
    dbFile = 'my_database.db'
    # データベースに接続
    con = sqlite3.connect(dbFile)

    # sqliteを操作するカーソルオブジェクトを作成
    cur = con.cursor()

    # テーブルの全データを取得
    cur.execute('SELECT tag_id FROM article')
    rows = cur.fetchall()

    # 取得したデータを配列に入れるために配列作り
    Change_array = []

    # 取得したデータを配列化
    for row in rows:
        n = row[0]
        print(n)
        Change_array.append(n)

    # カウント用のラベル
    labels = ['Python', 'Ruby', 'Java', 'PHP', 'JavaScript']

    # 各ラベルを 0 で初期化
    Count_tag = collections.Counter({label: 0 for label in labels})

    # 実際のカウントを追加
    Count_tag.update(Change_array)

    # dict_values をリストに変換
    count_tag_list = [Count_tag[label] for label in labels]

    # データベースの接続を切断
    cur.close()
    con.close()
    
    plt.pie(count_tag_list, labels=labels, autopct='%.f%%', labeldistance=None)
    plt.legend()
    plt.title('Language')
    
    buf = BytesIO()
    plt.savefig(buf, format="png")
    
    #画像データをBase64にエンコード
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    #エンコードしたデータをHTMLに渡す
    return render_template('graph.html', enn=data,bou=bouData)

def bou():
    user = User.select
    user1 = User.select().where(User.age >= 10).count()
    user10 = User.select().where(User.age >= 10, User.age < 20).count()
    user20 = User.select().where(User.age >= 20, User.age < 30).count()
    user = [user1, user10, user20]
    label = ['10歳未満', '10代', '20代', '30代', '40代', '50代', '60代', '70代', '80代', '90代', '100歳以上']
   
    width = 0.35

    
    # グラフ描画
    fig = Figure()
    ax = fig.subplots()
    ax.bar(labels, user, width)
    
    # 画像をバッファに保存
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)  # バッファのポインタを先頭に戻す
    
    # 画像データをBase64にエンコード
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    buf.close()  # バッファを閉じる

#エンコードしたデータを返す
    return  data
