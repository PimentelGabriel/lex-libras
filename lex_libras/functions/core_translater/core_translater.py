from db.repository.dictionary_repository import DictionaryRepository

from lex_libras.dto.palavraCandidataDTO import palavraCandidataDTO
from lex_libras.functions.core_translater.functions.encontrarAlias import encontrarAlias

from .functions import *
import os

from lex_libras.spacyProxy import matcher


class CoreTranslater:
    lastQueryResult = None

    candidateWords = []
    isWordsFecthed = False
    isWordsChecked = False

    def __fetchCandidateWord(self):

        # palavrasDB = self.__dictionaryRepository.selectPalavras(lemmas)
        self.isWordsFecthed = True
        return None

    print(f"LEXLIBRAS_VERBOSE: {os.environ.get('LEXLIBRAS_VERBOSE')}")

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
        # print("Tchau")

    def getCandidateWord(self, Doc):
        return Doc._.candidateWords.get()

        lemmas = []
        for token in Doc:
            if token._.eh_corresponde:
                lemmas.append(token._.metaDados['palavra'])
                Doc._.candidateWords.addNewCandidateWord(
                    palavraCandidataDTO(
                        token.i,
                        token._.metaDados['palavra'],
                        1
                    )
                )

        return lemmas

    def analisar(self, Doc):
        captura = matcher(Doc)

        # Encontra Substantivos Compostos, monsta-os e os procura no BD
        for match in captura:
            palavra = Doc[match[1]:match[2]]

            size = Doc._.candidateWords.addNewCandidateWord(
                palavraCandidataDTO(
                    match[1],
                    palavra.text.upper(),
                    3
                )
            )

            Doc._.candidateWords.wordList[size-1].span = palavra

        # TRIAGEM DE PALAVRAS QUE VÃO PARA A GLOSA
        # Deve-se selecionar quais palavras da sentença deve ser considerada
        for token in Doc:
            removeConj(token)
            removeArt(token)
            removeAdp(token)

            # Seção de removedor de 2º geração
            removeNSubj(token)

            token._.metaDados['palavra'] = token.lemma_.upper()
            token._.metaDados['claseGramatical'] = token.pos_
            if token._.eh_corresponde:
                Doc._.candidateWords.addNewCandidateWord(
                    palavraCandidataDTO(
                        token.i,
                        token._.metaDados['palavra'],
                        1
                    )
                )

        print(
            f"\n\t wordList LENGTH: {len(Doc._.candidateWords.wordList)}\n\n"
        )
        # Verifica flexões alternativas de palavra para econtrá-las no banco de dados
        # Ex.: FALOU -> FALAR
        encontrarAlias(Doc)  # type: None

        print("PRINT NAS PALAVRAS CANDIDATAS PARA SEREM BUSCADAS NO BD (getCandidateWord):")
        print("APÒS encontrarAlias(Doc)")
        print(f"Length: {len(Doc._.candidateWords.get())}")
        print(Doc._.candidateWords.get())

        # print("For lemmas\n")
        # for token in Doc:
        #     print(token._.metaDados['palavra'])
        #     print(token._.eh_corresponde)
        #     print("-----")

        # Add função que monta as palavras compostas
        # Palavras que em PT-br são duas porém em LIBRAS são representada como uma (no caso um sinal)
        aglutinarPalavra(Doc)

        lemmas = Doc._.candidateWords.get()

        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            print("\n\n#lemmas")
            print(lemmas)
            print("#fim lemmas")

        # ==================================================

        # Buscar no banco se há sinal correspondente as palavras recebidas e lematizadas
        # Fazer uam raw query no SQLAlchemy usando o statment 'where palavra in (lemas[0], lemas[1], lemas[2], lemas[3])'

        # dictionary.selectPalavras(lemas):

        #
            print("Query from DB")

        palavrasDB = self.__dictionaryRepository.selectPalavras(lemmas)

        # Marcando quais palavras possui correspondente no BD

        ArrayPalavras = []
        try:
            [ArrayPalavras.append(dict(p)) for p in palavrasDB]  # type: ignore
        except Exception as e:
            print(e)

        Doc._.candidateWords.electWord(Doc, ArrayPalavras)

        print("Fasltly print of 'palavras'")
        [print(f"\t{token._.metaDados['palavra']}") for token in Doc]

        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            print("\tArrayPalavras")
            print(ArrayPalavras)

        # for palavra in ArrayPalavras:
        #     for token in Doc:
        #         if palavra['palavra'] == token._.metaDados['palavra']:
        #             token._.metaDados['existeSinalLibras'] = True
        #             token._.metaDados['claseGramatical'] = palavra['flag']

        # FAZENDO DATILOLOGIA
        for token in Doc:
            if not token._.metaDados['existeSinalLibras']:
                if os.environ['LEXLIBRAS_VERBOSE'] == "1":
                    print(token._.metaDados["palavra"])

                datilologiaP = ""
                for l in token._.metaDados['palavra']:
                    if token._.metaDados['palavra'].index(l) == 0:
                        datilologiaP = l
                    else:
                        datilologiaP += "-"+l
                token._.metaDados["palavra"] = datilologiaP
