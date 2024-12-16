from .user import user_bp
from .product import product_bp
from .push import order_bp
from .article import article_bp
from .graph import graph_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  article_bp,
  order_bp,
  graph_bp
]
