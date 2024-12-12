from flask import Blueprint, render_template, request, redirect, url_for # type: ignore
from datetime import datetime
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
    


    
    return render_template('graph.html' , bou=bouData)


# def enn():
    

#     return enn


def bou():
    
    labels = ['10代以下','20代','30代','40代','50代以上']
    means = [20, 34, 30, 35, 27]
    width = 0.35

    
    # グラフ描画
    fig = Figure()
    ax = fig.subplots()
    ax.bar(labels, means, width)
    
    # 画像をバッファに保存
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)  # バッファのポインタを先頭に戻す
    
    # 画像データをBase64にエンコード
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    buf.close()  # バッファを閉じる

#エンコードしたデータを返す
    return  data
