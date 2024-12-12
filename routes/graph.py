from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3
import collections

# Blueprintの作成
article_bp = Blueprint('article', __name__, url_prefix='/graph')


@article_bp.route('/enn')
def enn():
    
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

    # 配列をdict_valuesに変換
    Count_tag = collections.Counter(Change_array)

    # dict_values をリストに変換
    count_tag_list = list(Count_tag.values())

    # データベースの接続を切断
    cur.close()
    con.close()

    return render_template('graph.html')


@article_bp.route('/bou',)
def bou():


    
    return render_template('graph.html')
