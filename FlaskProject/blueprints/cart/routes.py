from flask import Blueprint, render_template

class Cart:
    def __init__(self):
        self.Cart_blueprint = Blueprint('cart', __name__, template_folder='templates')
        self.cart_routes()

    def cart_routes(self):
        @self.Cart_blueprint.route('/shopping-cart')
        def shopping_cart():
            return render_template('shopping-cart.html')
