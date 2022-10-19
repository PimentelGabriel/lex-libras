SELECT
    distinct(p.palavra) as palavra,
    c.nome,
    c.flag
FROM
    palavras AS p,
    classes_gramaticais AS c
WHERE
    p.palavra IN ( 'IR', 'VENCER', 'DENGUE') AND
    p.classe_gramatical like c.id
GROUP BY
    p.palavra;

SELECT distinct(p.palavra) as palavra, c.nome, c.flag FROM palavras AS p, classes_gramaticais AS c WHERE p.palavra IN ( 'IR', 'VENCER', 'DENGUE') AND p.classe_gramatical like c.id GROUP BY p.palavra;