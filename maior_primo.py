def ePrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero)):
        if numero % i == 0:
            return False
    return True



def maior_primo(numero):
    max_primo = 0

    for i in range(2, numero + 1):
        if ePrimo(i):
            max_primo = i

    return(max_primo)

#pegando o numero pro range
numero = input("Digite um numero inteiro : ")
numero = int(numero)

#chamando a função que da o maior primo
maior_primo(numero)