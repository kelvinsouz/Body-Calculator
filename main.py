from BMIcalculator import main as bmi_main
from TDEEcalculator import main as tdee_main

def main():
    print("Escolha uma opção")
    print("1. Calculadora de IMC")
    print("2. Calculadora de TMB (Taxa metabólica Basal)")
    escolha = input("Digite o número da opção escolhida: ")

    if escolha == '1':
        bmi_main()
    elif escolha == '2':
        tdee_main()
    else:
        print("Opção inválida. Tente novamente")

if __name__ == "__main__":
    main()