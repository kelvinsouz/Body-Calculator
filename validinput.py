def validinput(prompt, num1, num2):
    try:
        while True:

            print(prompt)
            valor = float(input(f"O valor deve estar situado entre {num1} e {num2}: ").replace(",", "."))

            if valor >= num1 and valor <= num2:
                return valor
                break
            else:
                print(f"\nNúmero inválido, digite um número entre {num1} e {num2}\n")

    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        quit()

def gencheck():
    while True:
        x = input("Digite (H) para homem, ou (M) para mulher: ").upper()
        if x == "M" or x == "H":
            return x
            break
        else:
            print("Entrada inválida. Você deve digitar a letra H ou M.")
