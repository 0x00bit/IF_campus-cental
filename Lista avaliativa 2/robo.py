x = int(input("Posição X inicial: "))
y = int(input("Posição Y inicial: "))

mov = input("Movimentos: ").upper()

movs = []
validos = 0

for m in mov:
    if m == 'U':
        y += 1
        movs.append(m)
        validos += 1
    elif m == 'D':
        y -= 1
        movs.append(m)
        validos += 1
    elif m == 'R':
        x += 1
        movs.append(m)
        validos += 1
    elif m == 'L':
        x -= 1
        movs.append(m)
        validos += 1
    elif m == 'O':
        x -= 1
        y += 1
        movs.append(m)
        validos += 1
    elif m == 'N':
        x += 1
        y += 1
        movs.append(m)
        validos += 1
    elif m == 'E':
        x += 1
        y -= 1
        movs.append(m)
        validos += 1
    elif m == 'W':
        x -= 1
        y -= 1
        movs.append(m)
        validos += 1

print(f"Posição inicial: ({x}, {y})")
print(f"Posição final: ({x}, {y})")
print(f"Movimentos válidos: {validos}")
print(f"Movimentos: {' '.join(movs)}")

if x > 0 and y > 0:
    quad_inicial = "I"
elif x < 0 and y > 0:
    quad_inicial = "II"
elif x < 0 and y < 0:
    quad_inicial = "III"
elif x > 0 and y < 0:
    quad_inicial = "IV"
else:
    quad_inicial = "Eixo"

x_final, y_final = x, y

if x_final > 0 and y_final > 0:
    quad_final = "I"
elif x_final < 0 and y_final > 0:
    quad_final = "II"
elif x_final < 0 and y_final < 0:
    quad_final = "III"
elif x_final > 0 and y_final < 0:
    quad_final = "IV"
else:
    quad_final = "Eixo"

print(f"Quadrante inicial: {quad_inicial}")
print(f"Quadrante final: {quad_final}")
