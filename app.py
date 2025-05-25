import os
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import db, User
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create database tables
with app.app_context():
    # Drop existing tables if they exist
    db.drop_all()
    # Create new tables
    db.create_all()
    # Create a default admin user
    admin = User(username='admin', email='admin@example.com', is_admin=True)
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        flash('Invalid email or password')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

def convert_kg_to_lb(kg):
    """Convert kilograms to pounds"""
    return kg * 2.20462

def convert_lb_to_kg(lb):
    """Convert pounds to kilograms"""
    return lb / 2.20462

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        weight = float(data['weight'])
        
        if data['from_unit'] == 'kg':
            result = convert_kg_to_lb(weight)
            return jsonify({
                'converted_weight': round(result, 2),
                'to_unit': 'lb'
            })
        else:
            result = convert_lb_to_kg(weight)
            return jsonify({
                'converted_weight': round(result, 2),
                'to_unit': 'kg'
            })
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

@app.route('/')
def index():
    return render_template('index.html')

def convert_kg_to_lb(kg):
    """Convert kilograms to pounds"""
    return kg * 2.20462

def convert_lb_to_kg(lb):
    """Convert pounds to kilograms"""
    return lb / 2.20462

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        weight = float(data['weight'])
        
        if data['from_unit'] == 'kg':
            result = convert_kg_to_lb(weight)
            return jsonify({
                'converted_weight': round(result, 2),
                'to_unit': 'lb'
            })
        else:
            result = convert_lb_to_kg(weight)
            return jsonify({
                'converted_weight': round(result, 2),
                'to_unit': 'kg'
            })
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
