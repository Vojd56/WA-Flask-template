from flask import Blueprint, render_template

products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static')

@products_bp.route('/products')
def index():
    return render_template('products/products.html')
