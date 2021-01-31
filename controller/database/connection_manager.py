from psycopg2 import connect, extensions, sql

from configuration import USER, PASSWORD
from settings import HOST, DATABASE_NAME


class ConnectionManager:

    def __init__(self):
        self.connection = connect(
                host=HOST,
                user=USER,
                password=PASSWORD)
        self.connection.set_isolation_level(
                extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = None

    def execute(self, sql_statement):
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql_statement)
        self.cursor.close()

    def create_database(self):
        sql_statement = "CREATE DATABASE %s" % DATABASE_NAME
        return sql_statement
    
    def drop_database(self):
        sql_statement = "DROP DATABASE %s" % DATABASE_NAME
        return sql_statement
    

    # @classmethod
    # def use(cls):
    #     """Method that sets the appropriate database to use for
    #     the program.
    #     """
    #     statement = "USE %s" % DATABASE_NAME
    #     parameters = [statement, None]
    #     return parameters

    # def execute_one(self, parameters):
    #     """Method that execute a sql statement (provided
    #     by various modules methods) once.
    #     """
    #     self.open_cursor()
    #     self.cursor.execute(parameters[0], parameters[1])
    #     self.connection.commit()
    #     self.close_cursor()

