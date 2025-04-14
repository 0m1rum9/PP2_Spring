from database.connection import DbConnection

class Model:
    fillable = []
    hidden  = []
    table_name = ''
    where_query = {
        "values": [],
        "query" : [],
        'limit' : -1
    }
    connection = DbConnection()


    @classmethod
    def create(cls, fields : dict):
        model = cls()
        columns = ', '.join(model.fillable)
        try:
            values = tuple([fields[column] for column in model.fillable])

            with model.connection as cursor:
                cursor.execute(f"""
                    INSERT INTO {model.table_name} ({columns})
                    VALUES {values};
                """)
            print(f"Inserted {fields} ")
            return True
        except KeyError:
            print("Not all columns are provided")
            return False
    @classmethod
    def where(cls, column : str, operation : str, value=''):
        if value == '':
            value = operation
            operation = '='

        model = cls()


        if len(model.where_query['query']) > 0:
            model.where_query['query'].append('AND')

        model.where_query['query'].extend(([column, operation, "%s"]))
        model.where_query['values'].append(value)

        return model


    @classmethod
    def or_where(cls, column : str, operation : str, value=''):
        if value == '':
            value = operation
            operation = '='

        model = cls()
        model.where_query['values'].append(value)
        model.where_query['query'].extend(['OR', column, operation, "%s"])

        return model


    @classmethod
    def get(cls):
        model = cls()

        sql = f"SELECT * FROM {model.table_name}" + model.toSql(model.where_query)


        with model.connection as cursor:
            cursor.execute(sql, model.where_query['values'])
            data = cursor.fetchall()
        model.where_query = {
            "values": [],
            "query" : [],
            "limit" : -1
        }
        if len(data) == 1:
            data = data[0]
        return data

    @classmethod
    def all(cls):
        with cls.connection as cursor:
            cursor.execute(f"SELECT * FROM {cls.table_name};")
            data = cursor.fetchall()
        return data
    @staticmethod
    def toSql(query):

        where = ' '.join((query['query']))
        sql = f" WHERE {where}"
        if query['limit'] != -1:
            sql = sql + f" LIMIT {query['limit']}"

        return sql + ";"
    @classmethod
    def delete(cls):
        model = cls()

        sql = f"DELETE FROM {model.table_name} " + model.toSql(model.where_query)


        with model.connection as cursor:
            cursor.execute(sql, model.where_query['values'])

        model.where_query = {
            "values": [],
            "query" : [],
            "limit" : -1
        }

        return True
    @classmethod
    def update(cls, fields : dict):
        model = cls()
        values = [fields[column] for column in fields] + [where for where in model.where_query['values']]
        sets = ', '.join([column + " = %s" for column in fields])

        sql = f"UPDATE {model.table_name} SET {sets}" + model.toSql(model.where_query)

        with model.connection as cursor:
            cursor.execute(sql, values)
        print(f"UPDATED {fields}")
    @classmethod
    def limit(cls, limit : int):
        cls.where_query['limit'] = limit
        return cls()
# UPDATE users
# SET name = 'Almansur'
# WHERE id = 5