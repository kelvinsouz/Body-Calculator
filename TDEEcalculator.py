from validinput import validinput, gencheck

def tdeecalcM(peso, altura, idade, atividade, genero):

    alturacm = altura * 100
    if genero == "H":
        tdee = 88.36 + (13.4 * peso) + (4.8 * alturacm) - (5.7 * idade)
    else:
        tdee = 447.6 + (9.2 * peso) + (3.1 * alturacm) - (4.3 * idade)

    atividade_fatores = {
        1: 1.2,   # Sedentário
        2: 1.375, # Atividade física leve
        3: 1.55,  # Atividade física moderada
        4: 1.725  # Atividade física intensa
    }

    if atividade in atividade_fatores:
        fator = atividade_fatores[atividade]
    tdee *= fator
    return tdee

def main():
    print("Bem vindo ao programa de cálculo de TMB(Taxa metabólica Basal)")
    print("Você é um homem ou uma mulher?")
    genero = gencheck()
    peso = validinput("Informe o seu peso em quilos: ", 30, 300)
    altura = validinput("Informe sua altura em metros: ", 1.30, 2.50)
    idade = validinput("Informe a sua idade: ", 18, 90)
    print("Por fim, selecione o número que corresponde ao seu estilo de vida: ")
    print("(1) Sedentário (Trabalho de escritório)")
    print("(2) Atividade física leve (1-2 vezes por semana)")
    print("(3) Atividade física moderada (3-5 vezes por semana)")
    print("(4) Atividade física intensa (6-7 vezes por semana\n")
    atividade = validinput("Informe sua frequência de atividades físicas: ", 1, 4)
    tmb = tdeecalcM(peso, altura, idade, atividade, genero)
    print(f"{tmb:.2f}")

