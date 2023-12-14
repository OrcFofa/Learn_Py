i = input("digite a largura: ")
i = int(i)

j = input("digite a altura: ")
j = int(j)

condicao = 0
inicio = 0
meios = 0

while condicao < j:

     if inicio == 0:
          print(i * "#")
          inicio += 1

     elif meios == 0:
          vezes = i - 4
          for medida in range(j - 2):
               print("#",vezes * " ","#")
          meios = 1
    
     else:
          print(i * "#")
          break
          
       