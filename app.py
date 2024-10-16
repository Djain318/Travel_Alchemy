from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from datetime import datetime
from dotenv import load_dotenv
import genai
import os

load_dotenv()
secret_key = os.getenv("SECRET_KEY")

# Initialize Flask app
app = Flask(__name__)

# Set secret key and database URI for the app
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Load user by ID for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Define User model for database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    # Hash the user's password
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Verify the user's password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

# Create tables in the database
with app.app_context():
    db.create_all()

# Render the welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Handle user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullName = request.form.get('fullName')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check for missing fields
        if not fullName or not email or not password:
            flash('Please fill out all fields.','info')
            return redirect(url_for('register'))
        
        # Check if email is already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please login.', 'info')
            return redirect(url_for('login'))

        # Add new user to the database
        new_user = User(fullName=fullName, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to login after registration
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
        # Option 2: Automatically log in and redirect to index
        # login_user(new_user)
        # flash('Registration successful! You are now logged in.', 'success')
        # return redirect(url_for('index'))

    return render_template('welcome.html')

# Handle user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Find and authenticate user
        user = User.query.filter_by(email=email).first()

        if not user:
            flash('No User Found. Please Register', 'error')
            return redirect(url_for('register'))

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index')) 
        
        flash('Invalid credentials', 'error')
        return redirect(url_for('login'))

    return render_template('welcome.html') 

# Handle user logout
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('welcome'))


# Handle the main page and itinerary generation
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source = request.form.get('source', '')
        destination = request.form.get('destination', '')
        start_date = request.form.get('start_date', '')
        end_date = request.form.get('end_date', '')
        instructions = request.form.get('instructions', '')

        # Generate itinerary and handle date validation
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
            if end_date_obj < start_date_obj:
                raise ValueError("End date cannot be earlier than start date.")

            # Construct the hotel search URL
            hotel_url = (
                f"https://www.kayak.co.in/hotels/{destination}/{start_date_obj}/{end_date_obj}/2adults;map?sort=rank_a"
            )
            
            # Show generated itinerary
            plan = genai.generate_itinerary(source, destination, start_date, end_date, instructions)
            return render_template('index.html', plan=plan, hotel_url=hotel_url)  
       
        # Handle errors
        except Exception as e:
            return render_template('index.html', error=str(e))  
    # Show main page with no plan initially
    return render_template('index.html', plan=None)  

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
