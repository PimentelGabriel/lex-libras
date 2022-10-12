# from db.repository.class_word_repository import ClassWordRepository
# from db.repository.dictionary_repository import DictionaryRepository

from lex_libras.engine import TradutorLexLibras


tradutorLexLibras = TradutorLexLibras()

tradutorLexLibras.traduzir("Vamos combater dangue")

print(tradutorLexLibras.glosaVlibras)
print(tradutorLexLibras.docSpaCy)
# repo = DictionaryRepository()
# data = repo.select()

# print(data[0])
