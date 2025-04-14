class Blueprint:
    columns : dict
    active_column : str
    foreign_key = {}
    def __init__(self):
        self.columns = {}
        self.active_column = ''
    def id(self):
        self.columns['id'] = ['BIGSERIAL PRIMARY KEY']
        self.active_column = 'id'
        return self
    def string(self, name : str, size=255):
        self.columns[name] = [f'VARCHAR({size})']
        self.active_column = name
        return self
    def nullable(self):
        self.columns[self.active_column].append('NULL')
        return self
    def unique(self):
        self.columns[self.active_column].append('UNIQUE')
        return self
    def foreign_id_for(self, foreign_table_name):
        self.columns[foreign_table_name[0:len(foreign_table_name) - 1] + "_id"] = ["INT UNIQUE"]
        self.foreign_key = {
            "table_name" : foreign_table_name,
            "foreign_key" : foreign_table_name[0:len(foreign_table_name) - 1] + "_id"
        }
        # print(foreign_table_name[0:len(foreign_table_name) - 1] + "_id")
        return self
    #.......other methods for creating tables

# table = Blueprint()
# table.foreign_id_for('PhoneBooks')
# print(table.foreign_key)