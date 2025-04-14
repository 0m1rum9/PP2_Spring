from Models.model import Model

class PhoneBook(Model):
    table_name = 'phonebook'
    fillable = ['name', 'surname', 'phone_number']
