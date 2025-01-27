idade = int(input("Qual sua idade? "))
if idade >= 18:
    print("Você é maior de idade!")
    if idade >= 65:
        print("Você é idoso.")
else:
    print("Você é menor de idade!")