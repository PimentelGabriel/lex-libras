# from db.repository.class_word_repository import ClassWordRepository
# from db.repository.dictionary_repository import DictionaryRepository

from lex_libras.engine import TradutorLexLibras


tradutorLexLibras = TradutorLexLibras()

tradutorLexLibras.traduzir("Vamos combater dangue, ele vai morrer")

print(tradutorLexLibras.glosaVlibras)
print(tradutorLexLibras.docSpaCy)

for w in tradutorLexLibras.docSpaCy:
    print(w._.metaDados['palavra'])
# repo = DictionaryRepository()
# data = repo.select()

# print(data[0])
