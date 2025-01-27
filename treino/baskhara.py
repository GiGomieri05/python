# -*- coding: utf-8 -*-

import math

inputs = input().split()
A = float(inputs[0])
B = float(inputs[1])
C = float(inputs[2])

# -b +-v/(b² - 4ac) /2a

if A != 0:
    delta = (B ** 2) - (4 * A * C)
    if delta >= 0:
        r1 = (-B + math.sqrt(delta)) / (2 * A)
        r2 = (-B - math.sqrt(delta)) / (2 * A)
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")