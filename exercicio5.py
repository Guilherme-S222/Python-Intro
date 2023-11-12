""" Propostas Desafios:

1 - Conta letras maísculas e minúsculas:
-> Escreva uma função em Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

2 - Lista com números pares e ímpares de uma lista:
-> Escreva uma função em Python para imprimir os números pares e impares em duas listas separadas para cada uma.

"""


# Verificação Letra maiúscula e minúscula
def check_char(text):
    type = {"Uppercase": 0, "Lowercase": 0}
    for char in text: 
        if char.isupper():
            type["Uppercase"] += 1
        elif char.islower():
            type["Lowercase"] += 1
    print("Texto original:", text)       
    print("Número de letras maiúsculas:", type["Uppercase"])
    print("Número de letras minúsculas:", type["Lowercase"])

check_char("A Melhor Forma De Prever o Futuro é Criá-lo")

""" ----- EXPLICAÇÃO DO CÓDIGO -----
- def check_char(text): - Define a função chamada check_char que recebe um parâmetro chamado text.

- type = {"Uppercase": 0, "Lowercase": 0} - Cria um dicionário chamado type com duas chaves: "Uppercase" e "Lowercase", ambas inicializadas com o valor zero. Este dicionário será usado para contar o número de letras maiúsculas e minúsculas.

- for char in text: - Inicia um loop que itera sobre cada caractere no texto fornecido.

- if char.isupper(): - Verifica se o caractere atual é uma letra maiúscula.

- type["Uppercase"] += 1 - Se o caractere for uma letra maiúscula, incrementa o contador correspondente no dicionário.

- elif char.islower(): - Se o caractere não for uma letra maiúscula, verifica se é uma letra minúscula.

- type["Lowercase"] += 1 - Se o caractere for uma letra minúscula, incrementa o contador correspondente no dicionário.

- print("Texto original:", text) - Imprime o texto original fornecido como argumento para a função.

- print("Número de letras maiúsculas:", type["Uppercase"]) - Imprime o número de letras maiúsculas contadas.

- print("Número de letras minúsculas:", type["Lowercase"]) - Imprime o número de letras minúsculas contadas.

- check_char("A Melhor Forma De Prever o Futuro é Criá-lo") - Chama a função check_char com um exemplo de texto.
"""


# Verifica número par ou ímpar
def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
            
        else:
            odd.append(number)

    return pairs, odd

print(check_numbers([1, 2, 4, 6, 5, 100, 7, 11, 20, 13]))

""" ----- EXPLICAÇÃO DO CÓDIGO -----
- def check_numbers(numbers): - Define a função check_numbers que recebe uma lista de números chamada numbers.

- pairs = [] e odd = [] - Inicializa duas listas vazias, pairs para armazenar números pares e odd para armazenar números ímpares.

- for number in numbers: - Inicia um loop que itera sobre cada número na lista fornecida.

- if number % 2 == 0: - Verifica se o número é par, usando o operador % para verificar se o resto da divisão por 2 é zero.

- pairs.append(number) - Se o número for par, adiciona-o à lista pairs.

- else: - Se o número não for par (ou seja, é ímpar), executa o bloco de código a seguir.

- odd.append(number) - Adiciona o número à lista odd se for ímpar.

- return pairs, odd - Retorna as duas listas, pairs e odd, como uma tupla.

- print(check_numbers([1, 2, 4, 6, 5, 100, 7, 11, 20, 13])) - Chama a função check_numbers com uma lista de números e imprime o resultado.
"""