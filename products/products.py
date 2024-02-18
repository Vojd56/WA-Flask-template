from flask import Blueprint, render_template
from API.api import *

products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static')

@products_bp.route('/products')
def index():
    r = ReadAllProducts()
    l = len(r)
    return render_template('products/products.html',length = l, products = r)
