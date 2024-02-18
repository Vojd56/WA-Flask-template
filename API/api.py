from flask import Blueprint, render_template
import requests
import json
api_bp = Blueprint('api_bp', __name__,
    template_folder='templates',
    static_folder='static')

URL_API = "https://fakestoreapi.com"

def ReadAllProducts():
     
    request = requests.get(f"{URL_API}/products")
    
    result = json.loads(request.text)
    return result

#def GetAllProducts():
#    return json.load(ReadAllProducts())
    

