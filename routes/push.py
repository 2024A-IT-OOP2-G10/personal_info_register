from flask import Blueprint, render_template, request, redirect, url_for
from models import Order, User, Product, Article
from datetime import datetime

# Blueprintの作成
order_bp = Blueprint('order', __name__, url_prefix='/orders')


@order_bp.route('/')
def list():
    articles = Article.select()
    return render_template('order_list.html', title='投稿一覧', items=articles)


@order_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        article_id = request.form['article_id']
        created_at = datetime.now()
        Article.create(user=user_id, article=article_id, created_at=created_at)
        return redirect(url_for('push.list'))
    
    users = User.select()
    articles = Article.select()
    return render_template('order_add.html', users=users, article=articles)


@order_bp.route('/edit/<int:order_id>', methods=['GET', 'POST'])
def edit(order_id):
    order = Order.get_or_none(Order.id == order_id)
    if not order:
        return redirect(url_for('order.list'))

    if request.method == 'POST':
        order.user = request.form['user_id']
        order.product = request.form['product_id']
        order.save()
        return redirect(url_for('order.list'))

    users = User.select()
    products = Product.select()
    return render_template('order_edit.html', order=order, users=users, products=products)
