idade = int(input("Qual sua idade? "))
ingresso = input("Você tem ingresso? (s/n): ").lower()

if idade >= 18 and ingresso == 's':
    print("Você pode entrar na festa!")
else:
    print("Você não pode entrar.")