from db.repository.dictionary_repository import DictionaryRepository

print("coreTranlater called")
class CoreTranslater:
    dictionary = None

    def __init__(sefl):
        self.dictionary = DictionaryRepository()
        # Select
        data = session.query(Dictionary).all()
        for row in data:
            print(row.word)

    def __enter__(self):
        self.dictionary = DictionaryRepository()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
            

    def analisar(self, Doc):
        lemas = []

        for token in Doc:
            lemas.append(token.lemma_.upper())

            token._.metaDados['palavra'] = token.lemma_.upper()
            token._.metaDados['claseGramatical'] = token.pos_

        # Buscar no banco se há sinal correspondente as palavras recebidas e lematizadas
        # Fazer uam raw query no SQLAlchemy usando o statment 'where palavra in (lemas[0], lemas[1], lemas[2], lemas[3])'
        dictionary.selectPalavras(lemas)
