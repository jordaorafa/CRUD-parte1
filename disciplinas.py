import pediçoes #função para importar dados de "pediçoes"

#DISCIPLLINAS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.
disciplina = [] #criação da lista que será usada nas funções do programa

def cadastro_disci(nome_disci, cod_disci): #função para adicioonar nova disciplina
    global disciplina
    for p , e in enumerate(disciplina): #caso o código da disciplina já esteja na lista, retorna falso
        if e[1] == cod_disci:
            return False
    disciplina.append([nome_disci, cod_disci]) #caso o código da disciplina não esteja na lista, retorna verdadeiro e é adicionado
    return True

def apagar_disci(cod_disci): #função para apagar dados da disciplina
    global disciplina
    for p , e in enumerate(disciplina):
        if e[1].lower() == cod_disci: #se o código estiver na lista, ele deleta todos os dados da disciplina
            del disciplina[p]
            return True

def consultar_disci(): #função para apresentar a lista de disciplinas que foram adicionadas na operação
    global disciplina
    print("="*80)
    print(" ")
    print("DISCIPLINA:")
    print(" ")
    for p , e in enumerate(disciplina):
        print("Disciplina: %s Código: %s" %(e[0], e[1])) #forma com

def atualizar_disci(cod_disci): #função para atualização dos dados da disciplina
    global disciplina
    for p , e in enumerate(disciplina): #procurar o código da disciplina, caso encontre, modifique os dados já existentes pelos novos
        if e[1].lower() == cod_disci:
            novo_nome = input("Digite o novo nome: ")
            novo_cod = input("Digite o novo CPF: ")
            disciplina[p][0] = novo_nome #modificando os dados existentes pelos novos
            disciplina[p][1] = novo_cod
            print(" ")
            print("="*80)
            print(" ")
            print("Atualização concluida com sucesso!")
            print(" ")

def marcar_disci(): #função para adicionar os dados da disciplina no arquivo definitivo
    global disciplina
    arquivo_disci = open("disciplinas.txt", "a", encoding = "utf-8") #abrindo arquivo de texto para adicionar dados sem apagar os já existentes
    for p, e in enumerate(disciplina):
        arquivo_disci.write("%d.Disciplina: %s Código: %s\n" %((p+1),e[0], e[1])) #forma como os dados devem ser gravados no arquivo definitivo
    arquivo_disci.close() #fechando arquivo de texto

def leitura_disci(): #função para leitura dos dados que estão no arquivo definitivo
    global disciplinas
    arquivo_disci = open("disciplinas.txt", "r", encoding = "utf-8") #abrindo arquivo de texto porém apenas para a leitura
    for g in arquivo_disci.readlines():
        print(g) #mostrando arquivo para leitura
    arquivo_disci.close() #fechando arquivo de texto
