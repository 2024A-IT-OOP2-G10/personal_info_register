from flask import Flask, render_template
from models import initialize_database
from routes import blueprints
import os

app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# 画像が保存されている場所（static/images/）
IMAGE_FOLDER = 'static/images'

# 画像ファイル名のリストを定義（今回は例として画像2つ）
images = ['image1.jpg', 'image2.jpg']

# ホームページのルート
@app.route('/')
def index():
    return render_template('index.html')

# ダッシュボードのルート
@app.route('/dashboard')
def dashboard():
    # 画像のフルパスをリストにして渡す
    image_paths = [os.path.join(IMAGE_FOLDER, img) for img in images]
    return render_template('graph.html', images=image_paths)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
