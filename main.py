from BMIcalculator import main as bmi_main

def main():
    print("Escolha uma opção")
    print("1. Calculadora de IMC")

    escolha = input("Digite o número da opção escolhida: ")

    if escolha == '1':
        bmi_main()
    else:
        print("Opção inválida. Tente novamente")

if __name__ == "__main__":
    main()