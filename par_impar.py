#uso try pra pegar a string
try:
   numero = input("Digite um numero inteiro: ")
   numero_int = int(numero)

   if numero_int % 2 == 0:
    print(f"O numero {numero_int} é par")
   else:
    print(f"O numero {numero_int} é ímpar")

except:
    print("Isso não é um numero inteiro")
    