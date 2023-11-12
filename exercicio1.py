"""
1 - Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.

2 - Escreva um programa em Python que leia quatro números e calcule a média entre esses números

"""
# Desafio 1
numero = int(input("Digite um número:\n"))
print(f"O número escolhido foi: {numero}\nO sucessor desse numero é: {numero + 1}\nO antecessor desse numero é: {numero - 1}")

# Desafio 2
note1 = float(input("Digite a primeira nota:\n "))
note2 = float(input("Digite a segunda nota:\n "))
note3 = float(input("Digite a terceira nota:\n "))
note4 = float(input("Digite a quarta nota:\n "))

media = (note1 + note2 + note3 + note4) /4

print(f"A média é: {media}")