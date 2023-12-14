def é_hipotenusa(numero):
    for i in range(1, numero + 1):
        for j in range(i, numero + 1):
            hipotenusa = (i ** 2 + j ** 2) ** 0.5
            if hipotenusa == numero:
                return True
    return False

def soma_hipotenusas(numero):
    resultado_soma = 0

    for i in range(2, numero + 1):
        if é_hipotenusa(i):
            resultado_soma += i
    
    return (resultado_soma)

#pegando o numero pro range
numero = input("Digite um numero inteiro : ")
numero = int(numero)

#chamando a função que da o maior primo
soma_hipotenusas(numero)