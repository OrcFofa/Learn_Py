a = input("Digite um numero inteiro: ")
b = input("Digite outro inteiro: ")
c = input("Digite mais inteiro: ")

#transformando em inteiros
a = int(a)
b = int(b)
c = int(c)

#verificando se são 1 numero a mais
if b > a and a < b and b < c :
    print("crescente")
else:
    print("não está em ordem crescente")