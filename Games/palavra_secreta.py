palavra = "outro"

menu = """ ===PALAVRA SECRETA===
Sera que voce vai conseguir adivinhar???
"""
print(menu)
tentativas = 0

while True:
    letra = input("Digite uma letra: ")
    letra = letra.lower()
    vezes = palavra.count(letra)

    if letra == palavra:
        print(f"Você adivinhou a palavra secreta era '{palavra}', você fez {tentativas} tentativas")
        print("PARABÉNS!!!")
        break
    elif letra in palavra:
        print(f"A letra '{letra}' aparece {vezes} vezes na palavra secreta")
        tentativas += 1
        print(f'Você fez {tentativas} tentativas até agora')
        print("\n")

    else:
        print("Essa letra não está na palavra secreta")
        tentativas += 1
        print(f'Você fez {tentativas} tentativas até agora')
        print("\n")
       