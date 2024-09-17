def validinput(prompt,num1,num2):
    try:
        while True:
            valor = float(input(prompt).replace(",", "."))
            print(f"O valor deve estar situado entre {num1} e {num2}.")
            if valor >= num1 and valor <= num2:
                return valor
                break
            else:
                print(f"Por favor, digite um número entre {num1} e {num2}")
    except ValueError:
        print("Entrada inválido. Por favor, insira um número válido.")