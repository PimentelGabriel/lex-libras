from lex_libras.dto import palavraCandidataDTO


class candidateWordsMNG():
    list = []
    isWordsFecthed = False
    isWordsChecked = False

    def addNewCandidateWord(self, tuple: palavraCandidataDTO):
        tuple.i = len(self.list)

        if tuple.peso > 10 or tuple.peso < 1:
            raise Exception(f"{tuple.peso} must to be beetwen 1 and 10.")

        self.list.append(tuple)

        # for word in self.list:

    def __defineWords(self, Doc):
        for i, token in enumerate(Doc):
            if token._.eh_corresponde:

                words = []
                # Separa as palavras candidatas (presente em list) relacionado ao token em questão
                for i, w in enumerate(self.list):
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
                        self.list[word[0]].elegido = 1
                        break
