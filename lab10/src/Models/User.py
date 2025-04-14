from Models.model import Model

class User(Model):
    fillable = ['username', 'score']
    table_name = 'users'