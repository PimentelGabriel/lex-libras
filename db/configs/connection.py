import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text


class DBConnectionHandler():
    def __init__(self):
        self.__connection_string = "mysql+pymysql://lex_libras:toor@192.168.2.101:3306/LEX_LIBRAS"
        self.__engine = self.__create_database_engine()
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()

    def __create_database_engine(self):
        engineEcho = True
        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            engineEcho = True
        else:
            engineEcho = False

        return create_engine(
            self.__connection_string,
            echo=engineEcho,  # Acesso de dados em mobo verboso
            future=False  # Verificar pq quando True, dar erro
        )

    def __get_engine(self):
        return self.__engine

    def runSQLRaw(self, query, data=[{"index": "index"}]):
        try:
            eng = self.__get_engine()
            conn = eng.connect()

            # return conn.execute("SELECT palavra FROM palavras LIMIT 3;")

            statement = text(query)

            print(F"\n\n\tLOG DO runSQLRaw\n\t{__file__ }\n\t {__doc__}")
            print(f"statement: {statement}")
            print(f"Tipo: {type(statement)}")
            print(f"query: {query}")
            print(f"Tipo: {type(query)}\n\n")

            if data[0]["index"] == "index":
                print("1º execute")

                return conn.execute(query)
            else:
                print("2º execute")
                result = []
                for line in data:
                    # print("Exeted")
                    result.append(conn.execute(statement, **line))

                return result
        except Exception as e:
            print(e)

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
