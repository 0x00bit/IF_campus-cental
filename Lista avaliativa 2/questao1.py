massa_inicial = float(input("Massa inicial (em gramas): "))

massa_atual = massa_inicial
tempo_total_segundos = 0

while massa_atual > 0.5:
    massa_atual /= 2
    tempo_total_segundos += 50

horas = tempo_total_segundos // 3600
minutos = (tempo_total_segundos % 3600) // 60
segundos = tempo_total_segundos % 60

print(f"Massa Inicial: {massa_inicial:.2f} gramas")
print(f"Massa Final: {massa_atual:.8f} gramas")
print(f"Tempo de Decaimento: {horas}:{minutos:02}:{segundos:02}")
