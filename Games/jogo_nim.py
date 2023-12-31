def computador_escolhe_jogada (n , m):
    computadorRemove = 1
    while computadorRemove != m:
         if (n - computadorRemove) % (m+1)== 0:
            return computadorRemove
         else:
            computadorRemove += 1
    return computadorRemove

def usuario_escolhe_jogada (n , m) :
    boolean_verif = False
    while not boolean_verif:
        retirada = input("Quantas peças você vai tirar? ")
        retirada = int(retirada)

        if retirada > m or retirada < 1:
            print("Oops! Jogada inválida! Tente de novo.")
            boolean_verif = False
        else:
            boolean_verif = True    
    return retirada

def partida():
    jogada_valida = False
    while not jogada_valida:
        n = input("Quantas peças? ")
        n = int(n)

        m = int(input("Limite de peças por jogada? "))
        m = int(m)

        if m > n:
            print("\nOops! Número de peças a retirar inválido! Tente de novo.\n")
        else:
            jogada_valida = True

def partida():
    pecas_validas = False
    while not pecas_validas:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if m > n:
            print("\nOops! Número de peças a retirar inválido! Tente de novo.\n")
        else:
            pecas_validas = True
    vezDoPC = False
    if n % (m+1) == 0:
        print()
        print("Voce começa!")
    else:
        print()
        print("Computador começa!")
        vezDoPC = True
    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print("O computador tirou uma peça")
            else:
                print()
                print(f"O computador tirou {computadorRemove} peças")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return 2
            vezDoPC = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print("Você tirou uma peça")
            else:
                print()
                print(f"Você tirou {jogadorRemove} peças")
            if n == 0:
                print("Fim do jogo! Voce ganhou!") #nunca vai aparecer kkkkkkkkkkkkkkkk
                return 1
            vezDoPC = True
        if n ==1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print(f"Agora restam {n} peças no tabuleiro.")
                print()

            

def campeonato():
    pontuacao = usuario_pontos = computador_pontos = 0
    i = 1
    while i <= 3:
        print(f"**** Rodada {i} ****\n")
        pontuacao = partida()
        if pontuacao == 1:
            usuario_pontos += 1
        elif pontuacao == 2:
            computador_pontos += 1
        i+= 1
   
    print("\n**** Final do campeonato! ****")
    print(f"Placar: Você {usuario_pontos} X {computador_pontos} Computador\n")

#mostrando o menu
print('''Bem-vindo ao jogo do NIM! escolha: 
1 - para jogar uma partida isolada
2 - para jogar um campeonato 2''')

#pegando a opção
opção = input("\nEscolha uma opção: ")
opção = int(opção)

if opção == 1:
    print("\nVoce escolheu uma partida!")
    partida()
elif opção ==2:
    print("\nVoce escolheu um campeonato!")
    campeonato()
else:
    print("\nOops! opção inválida! Tente de novo.\n")