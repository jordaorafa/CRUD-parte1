import pediçoes #função para importar dados de "pediçoes"

#TURMA:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
turma = [] #criação da lista que será usada nas funções do programa

def cadastro_turma(cod_turma, periodo, cod_disci, cpf_prof, cpf_aluno): #funçao para adicionar nova turma
    global turma
    for p, e in enumerate(turma): #caso o codigo da turma ja esteja na lista, retorna falso
        if e[0] == cod_turma:
            return False    
    turma.append([cod_turma, periodo, cod_disci, cpf_prof, cpf_aluno]) #caso o codigo da turma nao esteja na lista, retorna verdadeiro e é adicionado
    return True

def apagar_turma(cod_turma): #funçao para apagar dados da turma da lista
    global turma
    for p, e in enumerate(turma):
        if e[0] == cod_turma: #se o codigo da turma estiver na lista, ele deleta todos os dados da turma
            del turma[p]
            return True
        
def consultar_turma(): #funçao para apresentar lista das turmas que foram adicionados na operaçao
    global turma
    print("="*80)
    print(" ")
    print("TURMA: ")
    print(" ")
    for p, e in enumerate(turma):
        print("Código da Turma: %s\nCódigo da Disciplina: %s\nPeríodo: %s\nCPF do Professor: %s\nCPF do Aluno: %s" %(e[0],e[1],e[2],e[3],e[4])) #forma como devem ser mostradas as informaçoes
        print(" ")

def atualizar_turma(cod_turma): #funçao para atualizaçao dos dados da turma
    global turma
    for p, e in enumerate(turma):
        if e[0] == cod_turma: #procurar o codigo da turma na lista, caso encontre, mosdifque os dados ja existentes pelos novos
            novo_cod_turma = input("Digite o novo código da turma: ")
            novo_cod_disci = input("Digite o novo código de disciplina: ")
            novo_periodo = input("Digite o período: ")
            novo_cpf_prof = input("Digite o CPF do professor: ")
            novo_cpf_aluno = input("Digite o CPF do aluno: ")
            turma[p][0] = novo_cod_turma #modificando os dados já existentes pelos novos
            turma[p][1] = novo_cod_disci
            turma[p][2] = novo_periodo
            turma[p][3] = novo_cpf_prof
            turma[p][5] = novo_cpf_aluno
            
def marcar_turma(): #funçao para adicionar os dados da turma no arquivo definitivo
    global turma
    arquivo_turma = open("turmas.txt", "a", encoding = "utf-8") #abrindo arquivo de texto para adicionar dados sem apagar os já existentes
    for p, e in enumerate(turma):
        arquivo_turma.write("Código da Turma: %s\nCódigo da Disciplina: %s\nPeríodo: %s\nCPF do Professor: %s\nCPF do Aluno: %s" %(e[0],e[1],e[2],e[3],e[4])) #forma como os dados devem ser adicionados no arquivo definitivo
    arquivo_turma.close() #fechando arquivo de texto

def leitura_turma(): #funçao para leitura dos dados que estao no arquivo definitivo
    global turma
    arquivo_turma = open("turmas.txt", "r", encoding = "utf-8") #abrindo arquivo de texto porem apenas para a leitura
    for g in arquivo_turma.readlines():
        print(g) #mostrando arquivo para leitura
    arquivo_turma.close() #fechando arquivo de texto

def ata(): #funçao para gerar ata de exercicio 
        global turma
        cod_turma = pediçoes.ped_cod_turma() #pediçoes para solicitaçao de dados da turma
        cod_disci = pediçoes.ped_cod_disci()
        periodo = pediçoes.ped_periodo()
        nome_aluno = pediçoes.ped_nome_aluno()
        cpf_aluno = pediçoes.ped_cpf_aluno()
        cpf_prof = pediçoes.ped_cpf_prof()
        print("="*80) #forma como deve ser gerada a ata de exercicio
        print(" ")
        print("Código da Disciplina: %s Código da Turma: %s" %(cod_turma, cod_disci))
        print(" ")
        print("="*80)
        print(" ")
        print("Período: %s CPF do Professor: %s" %(periodo, cpf_prof))
        print(" ")
        print("="*80)
        print(" ")
        print("Aluno: %s CPF: %s" %(nome_aluno, cpf_aluno))
        print(" ")
        print("="*80)
        print(" ")
        print("Nota:_________ Assinatura:________________________")
        print(" ")