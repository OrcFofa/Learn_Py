#Achando o primeiro digito
cpf_enviado = input("Digite o CPF sem os pontos: ")
nove_digitos = cpf_enviado[:9]
contador_regressivo_1 = 10
resultado_1_digito = 0

for digito in nove_digitos:
    resultado_1_digito += int(digito) * contador_regressivo_1 #Multiplicar e somando os 9 digitos
    contador_regressivo_1 -= 1
digito = (resultado_1_digito * 10) % 11 #Multiplicar e pegando o resto
digito = digito if digito <= 9 else 0 #verificação ternario pra ver se o numero é maior q 9
#print(digito)


#Achando o segundo digito
contador_regressivo_2 = 11
resultado_2_digito = 0

for digito_2 in nove_digitos:
    resultado_2_digito += int(digito_2) * contador_regressivo_2 #pegando os 9 numeros
    contador_regressivo_2 -= 1

digito_2 = ((10*(resultado_2_digito + (digito*2)))%11) #pegando o primeiro digito, somando, multiplicando e pegando o resto
digito_2 = digito_2 if digito_2 <= 9 else 0
#print(digito_2)


#Verificando se o CPF é valido
cpf_calculado = f"{nove_digitos}{digito}{digito_2}"

if cpf_calculado == cpf_enviado:
    print(f"O CPF {cpf_calculado} é valido")
else:
    print(f"O CPF {cpf_calculado} é invalido")