from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
   db = 'recipes'
   def __init__(self, data):
      self.id = data['id']
      self.name = data['name']
      self.description = data['description']
      self.instruction = data['instruction']
      self.under_30 = data['under_30']
      self.date_made = data['date_made']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

   @classmethod
   def create_recipe(cls, data):
      query = """
      INSERT INTO recipes (name, description, instruction, under_30, date_made)
      VALUES (%(name)s, %(description)s, %(instruction)s, %(under_30)s, %(date_made)s)
      ;"""
      return connectToMySQL(cls.db).query_db(query, data)

   @classmethod
   def update_recipe(cls,data):
      query = """
      UPDATE recipes 
      SET ( name=%(name)s, 
            description=%(description)s, 
            instruction=%(instruction)s, 
            date_made=%(date_made)s 
            under_30=%(under_30)s  )
      ;"""
      return connectToMySQL(cls.db).query_db(query, data)

   @classmethod
   def destroy_recipe(cls, data):
      query = '''
      DELETE FROM recipes
      WHERE id = %(id)s
      ;'''
      return connectToMySQL(cls.db).query_db(query, data)