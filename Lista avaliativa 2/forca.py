PALAVRA = "FLAMENGO" # Timão do coração, viva o Flamengo da Gama
palavra = PALAVRA.lower()

corretas = ['_'] * len(palavra)
erradas = []
tentativas = 6

while tentativas > 0 and '_' in corretas:
    print(" ".join(corretas))
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras erradas: {' '.join(erradas)}")
    
    letra = input("Digite uma letra: ").lower()
    
    if letra in erradas or letra in corretas:
        print("Você já tentou essa letra.")
        continue
    
    if letra in palavra:
        for i, char in enumerate(palavra):
            if char == letra:
                corretas[i] = letra
        print("Acertou!")
    else:
        erradas.append(letra)
        tentativas -= 1
        print("Errou!")

if '_' not in corretas:
    print(f"Parabéns! Você adivinhou a palavra: {PALAVRA}")
else:
    print(f"Game over! A palavra era: {PALAVRA}")
