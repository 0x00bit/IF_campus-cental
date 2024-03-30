print("="*30)
hora_partida, minuto_partida = input("Digite o horário de partida (Exemplo - 10:46) = ").split(":")
hora_chegada, minuto_chegada = input("Digite o horário de chegada (Exemplo - 21:23) = ").split(":")
tempo_descanso = int(input("Digite os segundos de descanso: "))
combustivel_gastos = input("Digite quantidade de combustível gasto: ")
preco_gasosa = float(input("Digite o preço litro: "))
distancia = float(input("Digite a distância percorrida: "))
print("="*30)
print("\n")

if(int(hora_chegada) > 24 or int(hora_partida) > 24):
    print("Horas inválidas!")
    quit()

if(int(minuto_chegada) > 60 or int(minuto_partida) > 60):
    print("Minutos inválidos!")
    quit()

if(tempo_descanso < 0 or int(combustivel_gastos) < 0):
    print("Tempo de descanso inválidas ou quantidade de combustível inválidas!")
    quit()

if(preco_gasosa < 0 or distancia < 0):
    print("Preço do combustivel ou distância inválidas!")
    quit()

tempo_viagem_segundos = (int(hora_chegada)-int(hora_partida))*3600
tempo_viagem_segundos += (int(minuto_chegada)-int(minuto_partida))*60
tempo_viagem_segundos += tempo_descanso

tempo_viagem = (int(hora_chegada)-int(hora_partida))
tempo_viagem += (int(minuto_chegada)-int(minuto_partida))/60

velocidade_media = distancia/tempo_viagem
velocidade_global = velocidade_media + tempo_descanso/3600

preco_viagem = distancia*preco_gasosa
desempenho = preco_gasosa/(distancia/float(combustivel_gastos))

print("="*30)
print(f"Tempo da viagem em segundos: {tempo_viagem_segundos}")
print(f"Velocidade média KM/h: {velocidade_media}")  # Falta adicionar velocidade global
print(f"Custo da viagem R$ {preco_viagem}")
print(f"Desempenho do carro: (R$/km) {desempenho}")
print("="*30)
