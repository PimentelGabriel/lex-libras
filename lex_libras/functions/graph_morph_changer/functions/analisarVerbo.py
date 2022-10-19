def analisarVerbo(token, Doc):
    # Obter flag do banco de dados para tratar adequadamente cada verbo
    if token._.clasePalavra == 'VERB-P':
        