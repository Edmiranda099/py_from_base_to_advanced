"""
Tuplas (tuple)

Tuplas são basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma nova tupla.

#Cuidado 1: as tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6, )
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6,
print(tupla2)

print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4,)
print(tupla4)

tupla5 = 4,
print(tupla5)

print(type(tupla5))

#CONCLUSÃO: podemos concluir que tuplas são definidas pela vírgula e não pelo uso de parênteses

(4) -> Não é tupla
(4, ) -> É tupla
4,    -> É tupla

# Podemos gerar uma tupla dinamicamente com range (inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))
"""

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desenpacotar.

# Métodos para adição e remoção de elementos nas tuplas são existem, dado o fato das tuplas serem imutáveis!
