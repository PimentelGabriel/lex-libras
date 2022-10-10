import nltk

texto = "Vamos combater a dengue!"

sentencas = nltk.sent_tokenize(texto, language="portuguese")

for frase in sentencas:
    print("\n\n================")
    print("Prase:\n"+frase)

    tokens = nltk.word_tokenize(frase, language="portuguese")
    print("Tokens:\n")
    print(tokens)

    tokensTagMorf = nltk.pos_tag(tokens, language="portuguese")
    print("Morfologic analise:\n")
    print(tokensTagMorf)
