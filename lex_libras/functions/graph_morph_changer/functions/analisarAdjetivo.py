import os

# Esse arquivo deve alterar os substantivo que são flexionados por genero, trocando o sufixo de genero para @  

def analisarAdjetivo(token, Doc):
    for w in token.children:
        if w.dep_ == 'amod':
            tamanho = len(w._.metaDados["palavra"])
            w._.metaDados["palavra"] = w._.metaDados["palavra"][:tamanho-1] + '@'

            if os.environ['LEXLIBRAS_VERBOSE'] == "1":
                print(f"A palavra {token.text} foi tornada neutra")