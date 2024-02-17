from flask import Blueprint, render_template
from API.api import ReadAllProducts
products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static')

@products_bp.route('/products')
def index():
    response = ReadAllProducts().json()
    
    return render_template('products/products.html', response=response)
