from db.configs.connection import DBConnectionHandler
from db.entities.class_word import ClassWord


class ClassWordRepository:
    def select(self):
        with DBConnectionHandler() as db:
            return db.session.query(ClassWord).all()
