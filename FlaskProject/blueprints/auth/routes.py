from flask import Blueprint, render_template, url_for, redirect, session, request, flash
from werkzeug.security import check_password_hash

from tools.database_connection import DatabaseConnection
from tools.user_admin_tools import UserAdminTools
from tools.sqli_tools import SQLInjectionTools


class User:
    def __init__(self):
        print("User class initialized")

        # Initialize database connection tools
        self.connection_tools = DatabaseConnection()
        self.connection_tools.connect_to_db()  # Establish the connection
        self.connection = self.connection_tools.connection  # Get the connection object

        # Pass the connection to UserAdminTools
        self.user_admin_tools = UserAdminTools(self.connection)

        # Initialize SQL Injection Tools
        self.sqli_tools = SQLInjectionTools()

        # Set up the Blueprint
        self.auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

        print("User class initialized")

        # Define routes
        self.users_auth_login_routes()
        self.users_auth_registration_routes()

    def users_auth_login_routes(self):
        print("login routes")

        @self.auth_blueprint.route('/login', methods=['GET'])
        def login_template():
            print("login template")
            if self.user_admin_tools.check_user_session():
                return redirect(url_for('catalog-page.html'))
            else:
                return render_template('login.html')

        @self.auth_blueprint.route('/login-request', methods=['POST'])
        def login_request():
            print("login request")
            if request.method == 'POST':
                email = request.form['email']
                password = request.form['password']

                # Check for SQL injection
                if self.sqli_tools.is_suspected_injection(email) or self.sqli_tools.is_suspected_injection(password):
                    flash("SQL Injection Detected")
                    return "SQL Injection Detected"

                # Fetch user from database
                user = self.user_admin_tools.get_user(email)
                print(user)
                if x := (user and check_password_hash(user['password'], password)):
                    print(x)
                    session['user'] = user['email']
                    return redirect(url_for('catalog-page.html'))
                else:
                    flash("Invalid Credentials", "danger")

            return render_template('login.html')

    def users_auth_registration_routes(self):
        @self.auth_blueprint.route('/registration')
        def register():
            return render_template('registration.html')
