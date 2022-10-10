from db.configs.connection import DBConnectionHandler
from db.entities.dictionary import Dictionary
from db.entities.class_word import ClassWord


class DictionaryRepository:
    def select(self):
        with DBConnectionHandler() as db:
            return db.session\
                .query(Dictionary, ClassWord)\
                .join(Dictionary, Dictionary.id_class_word == ClassWord.id_class)\
                .with_entities(
                    Dictionary.id,
                    Dictionary.word,
                    ClassWord.name_class,
                    Dictionary.path_video
                )\
                .all()
