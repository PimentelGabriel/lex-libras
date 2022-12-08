import os
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

    def selectPalavras(self, lemmas: list):
        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            print(f"Path {__file__}")
            print(f"Lemas recebido em selectPalavras: ")
            print(lemmas)

        palavrasCandidatas = ""
        # Fazer uam raw query no SQLAlchemy usando o statment 'where palavra in (lemas[0], lemas[1], lemas[2], lemas[3])'
        i = 0
        for palavra in lemmas:
            # Sanitizando as palavras
            # palavra.replace("'", "\\\'")
            # palavra.replace('"', '\\\"')

            if lemmas.index(palavra) == 0:
                if palavra.find("'"):
                    palavra = palavra.replace(r"'", "\\\'")
                palavrasCandidatas = f'\'{palavra}\''
            else:
                if palavra.find("'"):
                    palavra = palavra.replace(r"'", "\\\'")
                palavrasCandidatas += f', \'{palavra}\''

            if os.environ['LEXLIBRAS_VERBOSE'] == '1':
                print(f"In for: {i} - {palavra}")
                i += 1

        # print(f'SELECT distinct(palavra) FROM palavras WHERE palavra IN ({palavrasCandidatas})');
        print(os.environ['LEXLIBRAS_VERBOSE'])
        if os.environ['LEXLIBRAS_VERBOSE'] == '1':
            print("Palavras a serem pesquisadas no BD:")
            print(f"\n{palavrasCandidatas}")

        query = f'SELECT distinct(p.palavra) as palavra, c.nome, c.flag FROM palavras AS p, classes_gramaticais AS c WHERE p.palavra IN ({palavrasCandidatas}) AND p.classe_gramatical like c.id GROUP BY p.palavra;'

        result = None
        with DBConnectionHandler() as conn:
            # resp = conn.runSQLRaw("SELECT p.id, p.palavra, c.nome FROM palavras AS p, classes_gramaticais AS c IN ( :lemmas );", {"lemmas": palavrasCandidatas})
            resp = []
            try:
                resp = conn.runSQLRaw(query)
                self.lastResult = resp
                # print(query)

                # for r in resp:
                #     print(r)

            except Exception as e:
                print("\n### ERRO AO REALIZAR A QUERY: ###")
                print(e)
            # print(type(resp))
            # print(len(resp))

            return resp

        return []

        # for row in resp:
        #     print(row)

        # SELECT distinct(palavra) FROM palavras WHERE palavra IN ('IR', 'PARA', 'O', 'PRAIA')
