from validinput import validinput

def calcbmi(peso, altura):
    bmi = peso / (pow(altura, 2))
    return bmi

def bmiclassification(bmi):
    classifications = {
        (0, 16): "Classificação: Magreza severa",
        (16, 17): "Classificação: Magreza moderada",
        (17, 18.5): "Classificação: Magreza leve",
        (18.5, 25): "Classificação: IMC normal! Parabéns!",
        (25, 30): "Classificação: Sobrepeso",
        (30, 35): "Classificação: Obesidade I",
        (35, 40): "Classificação: Obesidade II"
    }

    for faixa, classificacao in classifications.items():
        if faixa[0] < bmi <= faixa[1]:
            print(classificacao)
            break
    else:
        print("Obesidade III")

def main():
    print("Bem vindo ao programa de Cálculo de IMC!")
    peso = validinput("Informe o seu peso em quilos.", 30, 300)
    altura = validinput("Agora, informe sua altura", 1.30, 2.50)
    imc = calcbmi(peso, altura)
    print("\nSeu IMC é de {:.2f}.".format(imc))
    classificacao = bmiclassification(imc)
