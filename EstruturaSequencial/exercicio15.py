salario_hora = float(input("Digite o valor do seu salário por hora: "))
horas = int(input("Digite a quantidade de horas trabalhadas: "))
salario_bruto = salario_hora * horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = inss + ir + sindicato
salario_liquido = salario_bruto - descontos

print(f"+ Salário bruto : R$ {salario_bruto:.2f}")
print(f"- IR (11%) : R$ {ir:.2f}")
print(f"- INSS (8%) : R$ {inss:.2f}")
print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
print(f"= Salário líquido : R$ {salario_liquido:.2f}")
