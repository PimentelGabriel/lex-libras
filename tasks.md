# Algoritimo de tradução PT-br para glosa LIBRAS
Por: Gabriel Pimentel de Castro Costa

## Passos

### Tradutor da palavra correspondente
Apesas de ser como um subgrupo de regras do PT-br, a LIBRAS tem suas particularidades não presente no PT-br por isso muitas palavras que há em PT-br não exsite em LIBRAS. Para isso devemos procurar um sinôonimo ou palavra correlacionada.

* Usar a biblioteca do NLTK para verificar isso por meio de similaridade de vetores representantes de palavras

```
    import nltk
```

* Caso não haja palavra correspndente deve-se usar a datilologia

### Alteração gráfica-mofológica
#### Âmbito Geral

Usando o spaCy

* Lematizar todas as palavras 

* Retirar grupo de palavras que não existe em LIBRAS usando a análise morfológica do spaCy
    Ex.: Artigos, conjunções

#### Ambito Específico
Usando o spaCy

* ##### Verbos
    Deve-se gravar no banco de dados as palavras em LIBRAS e uma coluna classificando o verbo armazenado
    Podendo ser: invariável, verbo classificador e conjugável

    * ###### Verbos conjugáveis
    Ao fazer uma análise morfológica obtem-se a congujação da pessoa que pratica o verbo e o objeto
    Após obter a pessoa deve-se concatenar a marcação junto ao verbo
    Ex.: 1pVERNCER2p
    Quer dizer que quem pratica a ação pe a 1º pessoa do singular para a 2 pessoa do plural
``` 
    As pessoas do descurso são 1, 2 e 3
    E ulilisa-se a letra 'p' para plural e 's' para singular
```

    * ###### Verbos classificadores (CL)
    Para cada verbo deve-se quem sofre a ação dele, por seguinte guardar junto ao token em questão (no caso, o verbo) a string concatenada do verbo e o objeto
    Ex.:
    PT-br               Glosa LIBRAS
    Eu corto o pão      EU PÂO CL <CORTAR-PÂO>

    Obs.: A particula CL, que indica que o verbo é classificador é adicionado em um nível superior para assim poder avaliar onde coloca-lo, pois só deve vir antes do verbo classificador, estando o verbo sozinho ou me grupo

    Ex.: ME@ MÃO [IXa] PÃO CL <CORTAR-PÃO> <ABRIR-PÃO> <PASSAR-MANTEIGA-NO-PÃO> <FECHAR-O-PÃO> aDAR1s

    * ###### Verbos invariáveis
    Usa-se o LEMA do verbo onb lugar dele.

### Reordenação sintática
    Reordenar as palavras já traduzida para as regras de LIBRAS
    Mapear o contexto em portugês para fazer a conversão corretamente pois LIBRAS não é puramente padronizada nesse sentido