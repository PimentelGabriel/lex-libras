from db.repository.dictionary_repository import DictionaryRepository

from .functions import *

class CoreTranslater:
    lastQueryResult = None

    def __init__(self):
        self.__dictionaryRepository = DictionaryRepository()
        return None
        # self.dictionary = DictionaryRepository()
        # Select
        # data = session.query(Dictionary).all()
        # for row in data:
        #     print(row.word)

    def __enter__(self):
        self.__dictionaryRepository = DictionaryRepository()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        None
        #print("Tchau")

    @staticmethod
    def returnPalavraElegida(Doc):
        lemmas = []
        for token in Doc:
            if token._.eh_corresponde:
                lemmas.append(token._.metaDados['palavra'])

        return lemmas

    def analisar(self, Doc):
        #TRIAGEM DE PALAVRAS QUE VÃO PARA A GLOSA
        # Deve-se selecionar quais palavras da sentença deve ser considerada
        for token in Doc:
            removeConj(token)
            removeArt(token)
            removeAdp(token)

            token._.metaDados['palavra'] = token.lemma_.upper()
            token._.metaDados['claseGramatical'] = token.pos_

        # print("For lemmas\n")
        # for token in Doc:
        #     print(token._.metaDados['palavra'])
        #     print(token._.eh_corresponde)
        #     print("-----")

        # print("\n\n#lemmas")
        # print(CoreTranslater.returnPalavraElegida(Doc))
        # print("#fim lemmas")

        # Buscar no banco se há sinal correspondente as palavras recebidas e lematizadas
        # Fazer uam raw query no SQLAlchemy usando o statment 'where palavra in (lemas[0], lemas[1], lemas[2], lemas[3])'
        # dictionary.selectPalavras(lemas)
        
        # 
        # self.__dictionaryRepository.selectPalavras(lemas)
