from flask import render_template, request, redirect, session, flash

from flask_app import app
from flask_app.models import user
from flask_app.models import recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def landing():
   return render_template('login.html')

@app.route('/register')
def register():
   return render_template('registration.html')

@app.route('/user/register', methods=['POST'])
def register_user():
   if not user.User.validate_user(request.form):
      return redirect('/register')
   data = {
      'email': request.form['email'],
      'first_name': request.form['first_name'],
      'last_name': request.form['last_name'],
      'password': bcrypt.generate_password_hash(request.form['password'])
   }
   id = user.User.create_user(data)
   session['user_id'] = id
   return redirect('/dashboard')

@app.route('/user/login', methods=['POST'])
def login_user():
   users = user.User.get_user_by_email(request.form)
   if not users:
      flash('Invalid Email')
      return redirect('/')
   if not bcrypt.check_password_hash(users.password, request.form['password']):
      flash('Invalid Password')
      return redirect('/')
   session['user_id'] = users.id
   return redirect('/dashboard')

@app.route('/dashboard')
def dashboard ():
   if 'user_id'  not in session:
      return redirect ('/logout')
   data = {
      'id': session['user_id']
   }
   users = user.User.get_user_by_id(data)
   recipes = recipe.Recipe.get_all_recipes(data)
   return render_template('dashboard.html', user = users, recipes = recipes)

@app.route('/logout')
def logout():
   session.clear()
   return redirect('/')
