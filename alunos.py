import pediçoes #função para importar dados de "pediçoes"

#ALUNOS:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
alunos = [] #criação da lista que será usada nas funções do programa

def cadastro_aluno(nome_aluno, cpf_aluno): #função para adicionar novo aluno
    global alunos
    for p, e in enumerate(alunos): #caso o cpf já esteja na lista, retorna falso
        if e[1] == cpf_aluno:
            return False
    alunos.append([nome_aluno, cpf_aluno]) #caso o cpf não esteja na lista, retorna veradeiro e é adicionado
    return True
    
def apagar_aluno(cpf_aluno): #função para apagar dados do aluno da lista
    global alunos
    for p, e in enumerate(alunos):
        if e[1] == cpf_aluno: #se o cpf etiver na lista, ele deleta todos os dados do aluno
            del alunos[p]
            return True

def consultar_aluno(): #função para apresentar lista de alunos que foram adicionados na operação
    global alunos
    print("="*80)
    print(" ")
    print("ALUNOS: ")
    print(" ")
    for p, e in enumerate(alunos):
        print("Aluno: %s CPF: %s" %(e[0],e[1])) #forma como devem ser mostradas as informações
    print(" ")

def atualizar_aluno(cpf_aluno): #função para atualização dos dados de aluno
    global alunos
    for p, e in enumerate(alunos):
        if e[1] == cpf_aluno: #procurar o cpf do aluno na lista, caso encontre, modifique os dados já existentes pelos novos
            novo_nome = input("Digite o novo nome: ")
            novo_cpf = input("Digite o novo CPF: ")
            alunos[p][0] = novo_nome #modificando os dados existentes pelos novos
            alunos[p][1] = novo_cpf

def marcar_aluno(): #função para adicionar os dados dos alunos no arquivo definitivo
    global alunos
    arquivo_alunos = open("alunos.txt", "a", encoding = "utf-8") #abrindo arquivo de texto para adicionar dados sem apagar os já existentes
    for p, e in enumerate(alunos):
        arquivo_alunos.write("%d. Aluno: %s CPF: %s\n" %((p+1),e[0],e[1])) #forma como os dados devem ser gravados no arquivo definnitivo
    arquivo_alunos.close() #fechando aquivo de texto

def leitura_aluno(): #função para leitura dos dados que estão no arquivo definitivo
    global alunos
    arquivo_alunos = open("alunos.txt", "r", encoding = "utf-8") #abrindo arquivo de texto porém apenas para a leitura
    for g in arquivo_alunos.readlines():
        print(g) #mostrando arquivo para leitura
    arquivo_alunos.close() #fechando arquivo de texto
        
