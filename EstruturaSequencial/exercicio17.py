area = int(input("Tamanho da área a ser pintada (em m²): "))

litro = area / 6
latas = litro / 18
galoes = litro / 3.6
valor_lata = latas * 80
valor_galoes = galoes * 25

print(f"Quantidade em latas de tinta: {latas:.2f}")
print(f"Quantidade em galoes de tinta: {galoes:.2f}")
print(f"Valor a ser pago em latas: R${valor_lata:.2f}")
print(f"Valor a ser pago em galoes: R${valor_galoes:.2f}")



