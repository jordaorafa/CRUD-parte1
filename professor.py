import pediçoes #função para importar dados de "pediçoes"

#PROFESSORES::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 
professor = [] #criação da lista que será usada nas funções do programa

def cadastro_prof(nome_prof, cpf_prof, departamento): #funçao para adicionar novo professor
    global professor
    for p , e in enumerate(professor): #caso o cpf já esteja na lista, retornar falso
        if e[1] == cpf_prof:
            return False
    professor.append([nome_prof, cpf_prof, departamento]) #caso o cpf não esteja na lista, retorna verdadeiro e adiciona na lista
    return True

def apagar_prof(cpf_prof): #funçao para apagar dados do professor da lista
    global professor
    for p , e in enumerate(professor):
        if e[1]  == cpf_prof: #se o cpf estiver na lista, ele deleta todos os dados do professor
            del professor[p]
            return True
            
def consultar_prof(): #função para apresentar lista dos professores que foram adicionados na operação
    global professor
    print("="*80)
    print(" ")
    print("PROFESSORES: ")
    print(" ")
    for p, e in enumerate(professor):
        print("%d.Professor: %s\nCPF: %s\nDepartamento: %s\n" %((p+1),e[0],e[1],e[2])) #forma como devem ser mostradas as informações
    print(" ")

def atualizar_prof(cpf_prof): #funçao para a atualizaçao dos dados do professor
    global professor
    for p, e in enumerate(professor):
        if e[1] == cpf_prof: #procurar o cpf do professor na lista, caso encontre, modifique os dados já existentes pelos novos
            novo_nome = input("Digite o novo nome: ")
            novo_cpf = input("Digite o novo CPF: ")
            novo_dep = input("Digite o novo departamento: ")
            professor[p][0] = novo_nome
            professor[p][1] = novo_cpf
            professor[p][2] = novo_dep

def marcar_prof(): #funçao para adicionar os dados do professor no arquivo de texto definitivo
    global professor
    arquivo_prof = open("professor.txt", "a", encoding = "utf-8") #abrindo arquivo de texto para adicionar dados sem apagar os já existentes
    for p, e in enumerate(professor):
        arquivo_prof.write("Professor: %s\n  CPF: %s Departamento: %s\n" %(e[0],e[1],e[2])) #forma como devem ser gravados os dados no arquivo definitivo
    arquivo_prof.close() #fechando arquivo de texto

def leitura_prof(): #funçao para leitura dos dados que estao no arquivo definitivo
    global professor
    arquivo_prof = open("professor.txt", "r", encoding = "utf-8") #abrindo arquivo de texto porem apenas para leitura
    for g in arquivo_prof.readlines():
        print(g) #mostrando arquivo para leitura
    arquivo_prof.close() #fechando arquivo de texto
