peso = float(input("Digite o peso: "))
excesso = peso - 50
multa = excesso * 4

print(f"Peso: {peso}kg")
print(f"Excesso: {excesso}kg")
print(f"Multa: R${multa:.2f}")
