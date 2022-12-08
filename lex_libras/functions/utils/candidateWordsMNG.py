from lex_libras.dto import palavraCandidataDTO


class candidateWordsMNG():
    def __init__(self) -> None:
        self.wordList = []
        self.disctincIndexList = []
        self.isWordsFecthed = False
        self.isWordsChecked = False

    def addNewCandidateWord(self, tuple: palavraCandidataDTO):
        tuple.i = len(self.wordList)

        found = False
        for w in self.wordList:
            if w.idToken == tuple.idToken:
                found = True
                break

        if not found:
            self.disctincIndexList.append(tuple.idToken)

        if tuple.peso > 10 or tuple.peso < 1:
            raise Exception(f"{tuple.peso} must to be beetwen 1 and 10.")

        self.wordList.append(tuple)

        # for word in self.list:

    def get(self) -> list:
        lemmas = []
        for lemma in self.wordList:
            lemmas.append(lemma.palavra)

        [print((t.palavra, t.idToken)) for t in self.wordList]
        print(self.disctincIndexList)

        return lemmas

    # Recebe o Doc e os lemmas que retornou do BD
    def electWord(self, Doc, lemmasFromDB: list):

        for lemma in lemmasFromDB:
            for w in self.wordList:
                print(
                    f"\t\tlemma['palavra'] == w.palavra => {lemma['palavra']} == {w.palavra}")
                if lemma['palavra'] == w.palavra:
                    w.elegido = 1
                    Doc[w.idToken]._.metaDados['claseGramatical'] = lemma['flag']
                    break

        print("self.wordList")
        [print(f'''{w.elegido},{w.palavra},{w.idToken}''')
         for w in self.wordList]

        for idToken in self.disctincIndexList:
            words = []

            for w in self.wordList:
                if w.idToken == idToken:
                    words.append(w)

            highestWeight = -1
            idTokenHightest = -1
            palavra: str = ''

            # Refatorar esse trecho de código
            for w in words:
                # Ibtendo o o id do token da palavra candidata com maior peso
                if highestWeight < w.peso and w.elegido > 0:
                    highestWeight = w.peso
                    idTokenHightest = w.idToken
                    palavra = w.palavra

            Doc[idTokenHightest]._.metaDados["palavra"] = palavra
            Doc[idTokenHightest]._.metaDados['existeSinalLibras'] = True

    def getElectedWords(self, Doc):
        for idToken in self.disctincIndexList:
            words = []
            for w in self.wordList:
                if w.idToken == idToken:
                    words.append(w)

            highestWeight = -1
            idTokenHightest = -1
            palavra: str = ''

            # Refatorar esse trecho de código
            for w in words:
                # Ibtendo o o id do token da palavra candidata com maior peso
                if highestWeight < w.peso and w.elegido > 0:
                    highestWeight = w.peso
                    idTokenHightest = w.idToken
                    palavra = w.palavra

            Doc[idTokenHightest]._.metaDados["palavra"] = palavra

            # indexList = []
            # for i in self.disctincIndexList:
            #     wighterWId = -1
            #     for w in self.wordList:
            #         if w.idToken == i:
'''
        for i, token in enumerate(Doc):
            if token._.eh_corresponde:

                words = []
                # Separa as palavras candidatas (presente em list) relacionado ao token em questão
                for i, w in enumerate(self.wordList):
                    if w.idToken == token.i:
                        words.append([i, w])

                hight = -1

                # Encontra o valor do maior peso
                for word in words:
                    if hight < word[1].peso:
                        hight = word[1].peso

                # Dentre as palavras com maior peso retira uma para fazer parte da glosa
                # Obs.: O método de escolha dessa palavras deve ser melhorado
                for word in words:
                    if word[1].peso == hight:
                        token._.metaDados["palavra"] = word.palavra

                        # Essa variavel diz respeito a versão da tradução que está sendo gerada
                        self.wordList[word[0]].elegido = 1
                        break
'''
