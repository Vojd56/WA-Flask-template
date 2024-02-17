from flask import Blueprint, render_template
import requests
api_bp = Blueprint('api_bp', __name__,
    template_folder='templates',
    static_folder='static')
URL_API = "https://fakestoreapi.com"

def ReadAllProducts():
    return requests.get(f"{URL_API}/products")
    
#@api_bp.route('/')
#def index():
#    return render_template('zatím nic')
