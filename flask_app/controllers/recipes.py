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
   # if not recipe.Recipe.validate_recipe(request.form):
   #    return redirect('/recipes/new')
   recipe.Recipe.create_recipe(request.form)
   return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
   if 'user_id' not in session:
      return redirect('/logout')
   data = {
      'id': id
   }
   user_data = {
      'id':session['user_id']
   }
   edit = recipe.Recipe.get_one_recipe(data)
   print(edit)
   return render_template('edit.html', edit = edit , user = user.User.get_user_by_id(user_data))

@app.route('/recipes/update', methods=['POST'])
def update_recipe():
   if 'user_id' not in session:
      return redirect('/logout')
   # if not recipe.Recipe.validate_recipe(request.form):
   #    print(request.form)
   recipe.Recipe.update_recipe(request.form)
   return redirect('/dashboard')


@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
   data = {
      'id':id
   }
   recipe.Recipe.destroy_recipe(data)
   return redirect('/dashboard')
