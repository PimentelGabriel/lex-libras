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
        return create_engine(
            self.__connection_string,
            echo=True,
            future=False  # Verificar pq quando True, dar erro
        )

    def __get_engine(self):
        return self.__engine

    def runSQLRaw(self, query, data=[{}]):
        eng = self.__get_engine()
        conn = eng.connect()
        
        statement = text(query)

        for line in data:
            return conn.execute(statement, **line)

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
