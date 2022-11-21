import os

def analisarSubsPlur(token):
    if token.pos_ == "NOUN" and token.morph.get("Number")[0] == "Plur":
        token._.metaDados["palavra"] = token._.metaDados["palavra"]+"++"
        
        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            print(f"O substantivo {token.text} foi alterado para a forma plural da glosa")
