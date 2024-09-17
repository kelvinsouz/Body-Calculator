from validinput import validinput
from BMIcalculator import calcbmi

print("Bem vindo ao programa de Cálculo de IMC!")
peso = validinput("Informe o seu peso em quilos.", 30, 300)
altura = validinput("Agora, informe sua altura", 1.30, 2.50)
print(calcbmi(peso, altura))
