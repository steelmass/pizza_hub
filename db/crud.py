import psycopg2
from db.parse import Parse

class DB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):

        con = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password)

        return con

    def insert(self, table_name: str, column: list, values: list) -> None:
        table_part = f'INSERT INTO {table_name} '
        column_part = f"({', '.join(column)}) VALUES "
        values_part = ''

        for field in values:
            part = '('

            for item in field:
                if type(item) == str:
                    part += "'" + item + "', "
                elif type(item) in (int, float):
                    part += str(item) + ', '
            part = part[:-2]
            part += '), '
            values_part += part

        req = table_part + column_part + values_part[:-2] + ';'

        print(req)

        try:
            con = self.connect()
            cur = con.cursor()
            cur.execute(req)
            con.commit()
            con.close()
        except EOFError as er:
            print(er)






