import pandas as pd

cadeira = []
df = pd.read_csv('materias.csv', header=None)


def atualizacao(arquivo):

    df.update(arquivo)


def adicionar():

    nome = input(" Nome da cadeira: ")
    cadeira.append(nome)
    return cadeira

def salvar():
    arquivo = open("materias.csv", "a+")
    arquivo.write(f"{cadeira}"+"\n")
    arquivo.close()
    return arquivo

def lista():
    arquivo = open("materias.csv", "r")
    for abrir in arquivo.readlines():
        print(abrir)
    arquivo.close()

def qtdlista(): # varrer colunas e linhas somando o núemro de itens

    itens = df.count().sum()

    print("linha(s) - Iten(s) na linha(s)\n")
    print(f"{df.count()}\n")
    print(f"Total de cadeiras na lista {itens}")

    return itens

def dataframe():

    print(df)


    return df

def testes():
    a = df[0]





def select():
    print("\nEscolha:\n" +
          "1 - Adcionar cadeira \n" +
          "2 - Olhar lista Antes de salvar \n" +
          "3 - Salvar\n" +
          "4 - Olhar Materias Salvas em arquivo\n"+
          "5 - Quantidade de itens na lista\n"+
          "6 - Visualizar DataFrame\n"+
          "7 - Testes"
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
        atualizacao(df)
        select()

    elif (escolha == 4):
        lista()
        select()

    elif (escolha == 5):
        qtdlista()
        select()

    elif (escolha == 6):
        dataframe()
        select()

    elif (escolha == 7):
        testes()
        select()

    else:
        print("Número inválido. Escolha um número válido")
        select()


    return select

#Principal

select()





