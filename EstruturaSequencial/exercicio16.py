area = int(input("Tamanho da área a ser pintada (em m²): "))

litro = area / 3
latas = litro / 18
valor = latas * 80

print(f"Quantidade de latas de tinta: {latas:.2f}")
print(f"Valor a ser pago: R${valor:.2f}")
