import pandas as pd

cadeira = []

def adicionar():
    nome = input(" Nome da cadeira: ")
    cadeira.append(nome)
    return cadeira

def salvar():
    arquivo = open("materias.txt", "a+")
    arquivo.write(f"{cadeira}"+"\n")
    arquivo.close()

def lista():
    arquivo = open("materias.txt", "r")
    for abrir in arquivo.readlines():
        print(abrir)
    arquivo.close()

def qtdlista():
    arquivo = open("materias.txt", "r")
    count = 0
    listas = arquivo.read()
    conteudo = listas.split(",")

    for list in conteudo:
        if list:
            count +=1
    print(f"\nQuantidade de itens contido na lista: {count}\n")

    return count
    arquivo.close()




def select():
    print("Escolha:\n" +
          "1 - Adcionar cadeira \n" +
          "2 - Olhar lista Antes de salvar \n" +
          "3 - Salvar\n" +
          "4 - Olhar Materias Salvas em arquivo\n"+
          "5 - Quantidade de itens na lista"
          )
    escolha = int(input(">>> "))

    if(escolha == 1):

        adicionar()
        select()

    elif(escolha == 2):
        print(cadeira)
        select()

    elif (escolha == 3):
        salvar()
        select()

    elif (escolha == 4):
        lista()
        select()

    elif (escolha == 5):
        qtdlista()
        select()

    elif ( escolha != int):
        select()

    else:
        print("Número inválido. Escolha um número válido")
        select()


    return select

#Principal

select()





