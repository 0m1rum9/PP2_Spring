from connection import DbConnection
from blueprint import Blueprint

class Scheme:
    @staticmethod
    def create(table_name, table : Blueprint):
        if not Scheme.isExists(table_name):
            connection = DbConnection()

            query = Scheme.toSql(table_name, table)

            with connection as cursor:
                cursor.execute(query)
            print(f"Created table {table_name}")
        else:
            print("Table already exists") 
    @staticmethod
    def toSql(table_name, table):
        columns = []

        for column_name in table.columns:
            column = [column_name]
            for attribute in table.columns[column_name]:
                column.append(str(attribute))
            columns.append(" ".join(column))
        columns = ','.join(columns)

        sql_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns} "
        if (len(table.foreign_key) > 0):
            sql_query += f", FOREIGN KEY ({table.foreign_key['foreign_key']}) REFERENCES {table.foreign_key['table_name']}(id) "
        return sql_query + ");"
    
    @staticmethod
    def isExists(table_name):
        connection = DbConnection()
        exists = False
        with connection as cursor:
            cursor.execute("""SELECT EXISTS (
                                SELECT 1
                                FROM information_schema.tables
                                WHERE table_schema = 'public'
                                  AND table_name = %s
                            );""", (table_name,))
            exists = cursor.fetchone()
        return False
    @staticmethod
    def drop(table_name):
        if Scheme.isExists(table_name):
            connection = DbConnection()
            with connection as cursor:
                cursor.execute(f"DROP TABLE {table_name};")
            print(f"Dropped {table_name}")
        else:
            print("Table does not exists")

# PHONEBOOK
# table = Blueprint()
# table.id()
# table.string('name').nullable()
# table.string('surname').nullable()
# table.string('phone_number').unique()
# Scheme.create('phonebook', table)

# USER
table = Blueprint()
table.id()
table.string('username').unique()
table.string('score')
Scheme.create('users', table)
# Scheme.drop("users"))