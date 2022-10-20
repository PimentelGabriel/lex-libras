# from db.repository.class_word_repository import ClassWordRepository
# from db.repository.dictionary_repository import DictionaryRepository

from lex_libras.engine import TradutorLexLibras


tradutorLexLibras = TradutorLexLibras()

# f1 = tradutorLexLibras.traduzir("Vamos vencer a dengue com um baixolão")
# f1 = tradutorLexLibras.traduzir("Vamos vencer a dengue!")

# into = "Vamos vencer a dengue!"
# glosa = "MOSQUITO VIR 1pVENCER2s"
# f1 = tradutorLexLibras.traduzir(into)

into = "O mosquito da dengue nasce e se desenvolve em água parada!"
glosa = "ÁGUA LARGAD@ MOSQUITO SURGIR DESENVOLVER"
f1 = tradutorLexLibras.traduzir(into)

print("\n\n\n\n")
print("[ENTRADA]: "+into)
print("[ESPERAD]: "+glosa)
print("[SAIDA-L]: "+f1)

# print(tradutorLexLibras.glosaVlibras)
# print(tradutorLexLibras.docSpaCy)

# for w in tradutorLexLibras.docSpaCy:
#     print(w._.metaDados['palavra'])

# repo = DictionaryRepository()
# data = repo.select()

# print(data[0])
