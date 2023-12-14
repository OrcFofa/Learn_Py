#criando nossa função
def bhaskara (a,b,c):
    #calculando o delta
    delta = (b**2) - (4*a*c)

    #verificando qual tipo de equação é
    if delta < 0:
        print("esta equação não possui raízes reais")

    elif delta == 0:
        raiz = -(b) / (2*a)
        print(f"a raiz dupla desta equação é {raiz}")
    else:
        #pegando os r1 e r2
        r1 = (((-1)*b) + (delta**0.5))/(2*a)
        r2 = (((-1)*b) - (delta**0.5))/(2*a)

        #organizando em ordem crescente
        if r1 < r2:
            print(f"as raízes da equação são {r1:.6f} e {r2:.6f}")
            
        else:
            print(f"as raízes da equação são {r2:.6f} e {r1:.6f}")


#pegando os valores de a, b e c
a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")
c = input("Digite o valor de c: ")

#convertendo
a = float(a)
b = float(b)
c = float(c)

#chamando a função
bhaskara(a,b,c)