arquivo = int(input("Tamanho do arquivo: (em MB): "))
velocidade = int(input("Velocidade do link (em MBPS): "))
tempo = (arquivo / velocidade) / 60
print(f"O tempo estimado para o download é de {tempo:.2f} minuto(s).")