from flask import Flask

from general.general import general_bp
from products.products import products_bp

app = Flask(__name__)

app.register_blueprint(general_bp)
app.register_blueprint(products_bp)

if __name__ == '__main__':
    app.run(debug=True, port=8001)