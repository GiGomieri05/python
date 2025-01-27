T = int(input())
inputs = input().split()
cont = 0

for cha in inputs:
    if int(cha) == T:
        cont += 1

print(cont)