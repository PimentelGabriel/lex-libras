import os

def analisarSubsPlur(token):
    if token.pos_ == "NOUN" and token.morph.get("Number")[0] == "Plur":
        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            print("\t\tNOUN PLUR "+token.text)
    
        token._.metaDados["palavra"] = token._.metaDados["palavra"]+"++"
