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

    def selectPalavras(self, lemmas):
        palavrasCandidatas = ''
        # Fazer uam raw query no SQLAlchemy usando o statment 'where palavra in (lemas[0], lemas[1], lemas[2], lemas[3])'
        for palavra in lemmas:
            if lemas.index(palavra) == 0:
                palavrasCandidatas = f'\'{palavra}\''
            else:       
                palavrasCandidatas += f', \'{palavra}\''

        F'SELECT distinct(palavra) FROM palavras WHERE palavra IN ({palavrasCandidatas})'

        SELECT distinct(palavra) FROM palavras WHERE palavra IN ('IR', 'PARA', 'O', 'PRAIA')