#Calculadora completa - Erick
import math

#Peça ao usuário para inserir seu peso e altura.

#Escreva seu peso em quilogramas
peso = float(input("Qual é o seu peso em quilogramas? "))

#Escreva sua altura em metros
altura = float(input("Qual é a sua altura em metros? (ex: 1.80) "))

#Pergunte ao usuário se ele está grávida.
gravida = input("Você está grávida? (s/n) ")

#Pergunte ao usuário sua idade.
idade = int(input("Qual é a sua idade? "))

#Calcule o IMC.
imc = peso / (altura ** 2)

#Imprime resultado do IMC.
print("Seu IMC é:", round(imc, 2))

#Classificação de IMC
if imc < 18.5:
    print("IMC entre 18,5 e 24,9 Kg/m2. Você está abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("IMC entre 18,5 e 24,9 Kg/m2. Você está com peso saudável.")
elif imc >= 25.0 and imc <= 29.9:
    print("IMC entre 25,0 e 29,9 Kg/m2. Você está com sobrepeso.")
elif imc >= 30.0 and imc <= 34.9:
    print("IMC entre 30,0 e 34,9 Kg/m2. Você está com obesidade grau I.")
elif imc >= 35.0 and imc <= 39.9:
    print("IMC entre 35,0 e 39,9 Kg/m2. Você está com obesidade grau II.")
else:
    print("IMC maior do que 40,0 Kg/m2. Você está com obesidade grau III.")

#Calcule a quantidade de água necessária.
quantidade_de_agua = math.floor(peso * 0.035)

#Imprima a quantidade de água necessária.
print("Você deve beber {} litros de água por dia.".format(quantidade_de_agua))

#Se a pessoa estiver grávida, aumente a quantidade de água necessária em 1 litro por dia.
if gravida == "s":
  quantidade_de_agua += 1

#Se a pessoa tiver menos de 18 anos, diminua a quantidade de água necessária em 0,5 litro por dia.
if idade < 18:
  quantidade_de_agua -= 0.5

#Imprima a quantidade de água necessária atualizada.
print("A quantidade de água necessária atualizada é: {} litros por dia. Esse valor será diferente caso você tenha menos de 18 anos.".format(quantidade_de_agua))
