# language: pt

Funcionalidade: Verificar se um retângulo colidiu com outro retângulo ou não.

Cenario: Um retângulo colidiu com outro.
    Dados dois retângulos nas coordenadas (6,7) (7,8) e dimensões (2,2) e (2,2)
    Quando quero saber se os retângulos colidiram.
    Entao o resultado é verdadeiro.

Cenario: Um retângulo não está colidingo com outro.
    Dados dois retângulos nas coordenadas (6,7) (2,5) e dimensões (2,2) e (2,2)
    Quando quero saber se os retângulos colidiram.
    Entao o resultado é falso.
