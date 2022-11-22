import os


def splitKeepSignal(string):
    minI = 0
    frases = []
    for i, l in enumerate(string, start=0):
        if l in ("!", "?", "."):  # Phrase separater
            frases.append(string[minI:i+1])
            minI = i+1

    # Deleting the blank space
    for i, frase in enumerate(frases, start=0):
        if frase[0] == " ":
            frases[i] = frase[1:]
        if frase[-1] == " ":
            frases[i] = frase[:-1]

    # print(frases)
    # if os.environ["LEXLIBRAS_VERBOSE"] == "1":
    #     print(frases)
    return frases
