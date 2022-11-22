import os
import sys
from lex_libras.engine import Preparer, TradutorLexLibras
from dotenv import load_dotenv
load_dotenv("./.env")


# from db.repository.class_word_repository import ClassWordRepository
# from db.repository.dictionary_repository import DictionaryRepository

try:
    print(os.environ['LEXLIBRAS_VERBOSE'])
except Exception as e:
    print(e)

preparer = Preparer()
tradutorLexLibras = TradutorLexLibras()

if '-v' in sys.argv:
    print("Verbose mode active!!!")
    os.environ['LEXLIBRAS_VERBOSE'] == "1"
    tradutorLexLibras.setVerboseMode(True)
else:
    tradutorLexLibras.setVerboseMode(False)

# f1 = tradutorLexLibras.traduzir("Vamos vencer a dengue com um baixolão")
# f1 = tradutorLexLibras.traduzir("Vamos vencer a dengue!")

# into = "Por isso precisamos fechar as caixas"
# glosa = "ENTÃO POR-ISSO CAIXA PRECISAR CL <TAMPAR-CAIXA>"
# f1 = tradutorLexLibras.traduzir(into)

# into = "Vamos vencer a dengue!"
# glosa = "MOSQUITO VIR 1pVENCER2s"
# f1 = tradutorLexLibras.traduzir(into)

# into = "O mosquito da dengue nasce e se desenvolve em água parada!"
# glosa = "ÁGUA LARGAD@ MOSQUITO SURGIR DESENVOLVER"
# f1 = tradutorLexLibras.traduzir(into)

into = "Tomar cuidado com vasos, garrafas, latas e pneus velhos!"
glosa = "CUIDADO OBJETO-ARREDONDADO-LONGO FLOR MARCADOR-1 VIDRO^OBJETO-CILÍNDRICO-ALONGADO MARCADOR-2 FERRO^OBJETO-MÉDIO MARCADOR-3 borracha^COISA- CIRCULAR VELH@"
glosa2 = "CUIDADO VASOS, GARRAFAS, LATAS E PNEUS VELH@!"
f1 = tradutorLexLibras.traduzir(into)


print("\n\n\n\n")
print("[ENTRADA]: "+into)
print("[ESPERAD]: "+glosa)
if glosa2 != None:
    print("[REALIST]: "+glosa2)
print("[SAIDA-L]: "+f1)

frase = None

ctl = True

while (ctl):
    print("\n\n\nDigite a frase para ser traduzida: ")
    frase = input()
    #f1 = tradutorLexLibras.traduzir(frase)

    f1 = preparer.translate(frase)

    print(f1)
    print("\n\n\nDeseja inserir uma nova frase? Sim = s ou Não = n")
    resp = input()
    if (resp == "n" or resp == "N"):
        ctl = False
        break
    else:
        os.system("clear")


# print(tradutorLexLibras.glosaVlibras)
# print(tradutorLexLibras.docSpaCy)

# for w in tradutorLexLibras.docSpaCy:
#     print(w._.metaDados['palavra'])

# repo = DictionaryRepository()
# data = repo.select()

# print(data[0])
