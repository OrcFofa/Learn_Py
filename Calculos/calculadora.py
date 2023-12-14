menu = '''======Calculadora=====
[1]Somar    [2]Subtrair
[3]Dividir  [4]Multiplicar
[5]Elevar   [6]Raiz quadrada
[7]Fatorial
[0]Sair'''

while True:
  print(menu)
  print(" ")
  choice = input("Digite o numero da sua operação: ")
  if choice == "1":
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    print(f"A soma do {numero1} com o {numero2} é {numero1 + numero2}")
    
  elif choice == "2":
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    print(f"A subtração do {numero1} com o {numero2} é {numero1 - numero2}")
    
  elif choice == "3":
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    print(f"A divisão do {numero1} com o {numero2} é {numero1 / numero2}")
    
  elif choice == "4":
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    print(f"A multiplicação do {numero1} com o {numero2} é {numero1 * numero2}")

  elif choice == "5":
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    print(f"A elevação do {numero1} com o {numero2} é {numero1 ** numero2}")

  elif choice == "6":
    numero1 = int(input("Digite um numero: "))
    print(f"A raiz quadrada do {numero1} é {numero1**(1/2)}")

  elif choice == "7":
    numero1 = int(input("Digite um numero: "))
    fatorial = 1

    if numero1 == 0:
     fatorial = 1

    elif numero1 > 0:
     for i in range(1, numero1+1):
        fatorial *= i
    print(f"O fatorial de {numero1} é {fatorial}")   

  elif choice == "0":
    print("Obrigada por usar minha calculadora, by Laura")
    break
  
  else:
    print("Escolha uma das opçoes")
    continue