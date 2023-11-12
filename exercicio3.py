# Desafio 1 - Cálculo da Distância

distancia = float(input("Qual a distância que a ser percorrida?\n"))

if distancia <= 200:
    total = distancia * 0.50
elif distancia > 200:
    total = distancia * 0.35
print(f"O custo total dessa viagem será de: R${total:.2f} reais ")


# Desafio 2

salarioAtual = float(input("Qual o valor do salário atual? \n"))

if salarioAtual > 1250:
    aumentoSalario = salarioAtual * 0.10
elif salarioAtual <= 1250:
    aumentoSalario = salarioAtual * 0.15
    
novoSalario = salarioAtual + aumentoSalario
print(f"O seu aumento será de: R${aumentoSalario:.2f} reais, totalizando seu novo salário: R${novoSalario:.2f} reais")