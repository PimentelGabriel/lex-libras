from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler():
    def __init__(self):
        self.__connection_string = "mysql+pymysql://root:@localhost:3306/LEX_LIBRAS"
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

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
