import math
from validinput import validinput, gencheck
def bfcalc(waist, neck, height, gender, hip):
    heightcm = height * 100
    if gender == "H":
        bf = (495 / (1.0324 - 0.19077 * (math.log10(waist - neck)) + 0.15456 * (math.log10(heightcm)))) - 450
    else:
        bf = (495 / (1.29579 - 0.35004 * (math.log10(waist+hip-neck)) + 0.22100 * (math.log10(heightcm)))) - 450
    return bf


def main():
    print("\nBem vindo ao programa de cálculo da taxa de gordura corporal!")
    print("Você é um homem ou uma mulher?")
    genero = gencheck()
    if genero == "M":
        quadril = validinput("Informe a medida do seu quadril: ", 60, 130)
    else:
        quadril = 0
    altura = validinput("\nInforme sua altura em metros: ", 1.30, 2.50)
    pescoco = validinput("\nInforme a medida do seu pescoço em centímetros: ", 20, 60)
    cintura = validinput("\nInforme a medida da sua cintura em centímetros: ", 50, 130)
    bf = bfcalc(cintura, pescoco, altura, genero, quadril)
    print(f"\nA sua porcentagem de gordura corporal é de aproximadamente {round(bf, 1)}%.")