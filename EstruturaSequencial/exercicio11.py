int1 = int(input("Digite um número inteiro: "))
int2 = int(input("Digite outro número inteiro: "))
real = float(input("Digite um número real: "))

a = (int1 * 2) + (int2 / 2)
b = (int1 * 3) + real
c = real ** 3

print(f"O produto do dobro do primeiro com a metade do segundo: {a}")
print(f"A soma do triplo do primeiro com o terceiro: {b}")
print(f"O terceiro elevado ao cubo: {c}")
