# A função LAMBDA pode ter quantos argumentos quanto possivel, porem só pode ter UMA expressão
# Em outros linguagens são chamadas de funções anonimas

# 1 - Função de potência de números
power = lambda num: num **2

# 2 - Função que verifica se o número é par
pair = lambda x: x % 2 == 0

# 3 - Função que divide o numero por outro
divNum = lambda x, y : x / y

# 4 - Função de inverte uma String
reverse = lambda s: s[::-1] 

print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divNum(10, 2))
print(divNum(6, 2))
print(reverse("Python"))
print(reverse("JavaScript"))