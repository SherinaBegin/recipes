from flask import render_template, request, redirect, session, flash

from flask_app import app
from flask_app.models import recipe
from flask_app.models import user

@app.route('/recipes/new')
def new_recipes():
   if 'user_id'  not in session:
      return redirect ('/logout')
   data = {
      'id': session['user_id']
   }
   users = user.User.get_user_by_id(data)
   return render_template('create.html', user = users)

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
   if 'user_id' not in session:
      return redirect('/logout')
   recipe.Recipe.create_recipe(request.form)
   return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
   data = {
      'id':id
   }
   recipe.Recipe.destroy_recipe(data)
   return redirect('/dashboard')
