
menu ='''=====Lista=====
[1]Adicionar
[2]Apagar
[3]Listar
[4]Sair
'''
print(menu)
lista = []


while True:
    escolha = input("Escolha uma opção: ")

    if escolha == "1": #criando o adicionar
        add = input("O que voce deseja adicionar? ")
        lista.append(f"{add}")
        print("Adicionado com sucesso")

    elif escolha == "2": #criando o apagar
        idx = input("Digite o index do intem: ")
        inteiro = int(idx)
        largura = len(lista)

        if inteiro >= 0 and inteiro <= largura:
            lista.pop(inteiro)
            print("Item apagado com sucesso")
        else:
            print("Esse item não existe")

    elif escolha == "3": #listando com index
        vazia = len(lista)

        if vazia > 0:
         for index, item in enumerate(lista):
            print("Index e Item")
            print(index, item)
        else:
            print("Lista vazia")

    elif escolha == "4": #encerrando
        print("Obrigada por usar a listinha by OrcFoca")
        break

    else:
        print("Digite uma opção valida")