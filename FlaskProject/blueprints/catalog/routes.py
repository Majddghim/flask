from flask import Blueprint, render_template

class catalog:
    def __init__(self):
        self.catalog_blueprint = Blueprint('cat', __name__, template_folder='templates')
        self.catalog_routes()
    def catalog_routes(self):
        @self.catalog_blueprint.route('/catalog-page')
        def catalog_page():
            print("Catalog page")
            return render_template('catalog-page.html')

        @self.catalog_blueprint.route('/product/<product_id>')
        def product_page(product_id):
            print("product page")
            return f"Details of Product {product_id}"
