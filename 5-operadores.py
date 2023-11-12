num1 = int(input("Digite o primeiro numero\n"))
num2 = int(input("Digite o segundo numero\n"))

# Operadores Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Soma de {num1} e {num2} = {sum}")
print(f"Subtração de {num1} e {num2} = {sub}")
print(f"Divisão de {num1} e {num2} = {div}")
print(f"Multiplicação de {num1} e {num2} = {mult}")
print(f"Resto da divisão de {num1} e {num2} = {mod}")
print(f"Exponenciação de {num1} e {num2} = {exp}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(bigger)
print(smaller)
print(equal)
print(different)
print(bigger_equal)
print(smaller_equal)

# Operadores de Atribuição
num1 += 1
num1 -= 1
num1 *= 1
num1 /= 1

