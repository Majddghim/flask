from flask import Flask, redirect
from blueprints.auth import auth_blueprint
from blueprints.catalog import catalog_blueprint
from blueprints.cart import Cart_blueprint

app = Flask(__name__)

app.secret_key='secret_key'
# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(catalog_blueprint, url_prefix='/catalog')
app.register_blueprint(Cart_blueprint, url_prefix='/cart')

@app.route('/')
def home():
    return redirect('/auth/login')

if __name__ == '__main__':
    app.run(debug=True)
