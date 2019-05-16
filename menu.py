import alunos 
import professor
import turmas
import disciplinas
import pediçoes
#funções para a importação de dados de"alunos", "professor", "turmas", "disciplinas" e "pediçoes"

#MENU PROFESSOR ================================================================================
def menu_prof(): #função para menu do professor
    print("""======= MENU DO PROFESSOR =======
(1) Adicionar
(2) Excluir
(3) Consultar
(4) Atualizar
(5) Gravar
(6) Lista Gravada
(0) Voltar para o menu principal""") 
    while True: #repetição sempre que for verdadeira
        op2 = int(input("Escolha uma opção: ")) #solicitação da escolha da opção do menu

        if op2 > 6 or op2 < 0: #só podem ser escolhidos números de 0 a 6
            print("Opção inválida, digite novamente.")
            continue
        if op2 == 1: #opção 1 feita para cadastro de um novo professor
            nome_prof = pediçoes.ped_nome_prof() #pediçoes para a solicitação de dados
            cpf_prof = pediçoes.ped_cpf_prof()
            departamento = pediçoes.ped_departamento()
            if professor.cadastro_prof(nome_prof, cpf_prof, departamento) == True: #caso seja verdadeiro mostrar que foi cadastrado
                print(" ")
                print("="*80)
                print(" ")
                print("Professor cadastrado com sucesso!")
                print(" ")
                menu_prof() #retornar menu do professor
            else: #caso seja falso mostrar que já tem cadastro
                print(" ")
                print("="*80)
                print("Professor já cadastrado!")
                print(" ")
                menu_prof() #retornar menu do professor

        elif op2 == 2: #opção 2 feita para deletar dados de um professor
            cpf_prof = pediçoes.ped_cpf_prof() #pedição para a solicitação do cpf do professor
            if professor.apagar_prof(cpf_prof) == True: #caso o cpf esteja na lista mostrar que foi deletado todos os dados desse professor
                print(" ")
                print("="*80)
                print(" ")
                print("Professor deletado!")
                print(" ")
                menu_prof() #retornar menu do professor
            else: #caso o cpf não esteja na lista mostrar que não foi encontrado
                print(" ")
                print("="*80)
                print(" ")
                print("Professor não encontrado!")
                print(" ")
                menu_prof() #retornar menu do professor
            
        elif op2 == 3: #opção 3 feita para a consulta dos dados do professor adicionados na operação
            professor.consultar_prof()
            menu_prof()
            
        elif op2 == 4: #opção 4 feita para atualização dos dados do professor
            cpf_prof = pediçoes.ped_cpf_prof() #pedição para a solicitação do cpf do professor
            if professor.atualizar_prof(cpf_prof) == True: #caso o cpf esteja na lista, mostrar que a atualização foi um sucesso
                print(" ")
                print("="*80)
                print(" ")
                print("Atualização concluida com sucesso!")
                print(" ")
            menu_prof() #retornar menu do professor

        elif op2 == 5: #opção 5 feita para adicionar dados no arquivo de texto definitivo
            professor.marcar_prof()
            menu_prof() #retornar menu do professor

        elif op2 == 6: #opção 6 feita para mostrar dados que já estão gravados no arquivo de texto
            professor.leitura_prof()
            menu_prof() #retornar menu do professor
                
        elif op2 == 0: #opção 0 feita para retornar para o menu principal
            menu_principal()

#MENU ALUNO =========================================================================================
def menu_aluno(): #função para o menu do aluno
    print("""======= MENU DO ALUNO =======
(1) Adicionar
(2) Excluir
(3) Consultar
(4) Atualizar
(5) Gravar
(6) Lista Gravada
(0) Voltar para o menu principal""") 
    while True: #repetição sempre que for verdadeira
        op3 = int(input("Escolha uma opção: ")) #solicitação da escolha da opçao do menu

        if op3 > 6 or op3 < 0: #só podem ser escolhidos números de 0 a 6
            print("Opção inválida, digite novamente.")
            continue
        if op3 == 1: #opçao 1 feita para o cadastro de um novo aluno
            nome_aluno = pediçoes.ped_nome_aluno() #pediçoes para a solicitaçao de dados
            cpf_aluno = pediçoes.ped_cpf_aluno()
            if alunos.cadastro_aluno(nome_aluno, cpf_aluno) == True: #caso seja verdadeira mostrar que foi cadastrado
                print(" ")
                print("="*80)
                print(" ")
                print("Aluno cadastrado com sucesso!")
                print(" ")
                menu_aluno() #retornar para o menu do aluno
            else: #caso seja falso mostrar que já tem cadastro
                print(" ")
                print("="*80)
                print(" ")
                print("Aluno já cadastrado!")
                print(" ")
                menu_aluno() #retornar menu do aluno
                
        elif op3 == 2: #opçao 2 deita para deletar dados de um aluno
            cpf_aluno = pediçoes.ped_cpf_aluno() #pedição para a solicitaçao do cpf do aluno
            if alunos.apagar_aluno(cpf_aluno) == True: #caso o cpf esteja na lista mostrar que foi deletado todos os dados desse aluno
                print(" ")
                print("="*80)
                print(" ")
                print("Aluno deletado!")
                print(" ")
                menu_aluno() #retornar menu do aluno
            else: #caso seja falso mostrar que o aluno nao foi encontrado
                print(" ")
                print("="*80)
                print(" ")
                print("Aluno não encontrado!")
                print(" ")
                menu_aluno() #retornar menu do aluno
                
        elif op3 == 3: #opção 3 feita para consultar os dados do aluno adicionados na operação
             alunos.consultar_aluno()
             menu_aluno()
             
        elif op3 == 4: #opçao 4 feita para atualização dos dados do aluno
            cpf_aluno = pediçoes.ped_nome_aluno() #pedição para solicitaçao do cpf do aluno
            if alunos.atualizar_aluno(cpf_aluno) == True: #caso o cpf esteja na lista mostrar que a atualização foi um sucesso
                print(" ")
                print("="*80)
                print(" ")
                print("Atualização concluida com sucesso!")
                print(" ")
            menu_aluno() #retornar menu do aluno

        elif op3 == 5: #opçao 5 feita para adicionar dados no arquivo de texto definitivo
            alunos.marcar_aluno()
            menu_aluno() #retornar menu do aluno

        elif op3 == 6: #opçao 6 feita para mostrar dados que já estao gravados no arquivo definitivo
            alunos.leitura_aluno()
            menu_aluno() #retornar menu do aluno
                
        elif op3 == 0:
            menu_principal() #retornar para o menu principal

#MENU DISCIPLINA ==============================================================================================
def menu_disci(): #funçao para menu da disciplina
    print("""======= MENU DA DISCIPLINA =======
(1) Adicionar
(2) Excluir
(3) Consultar
(4) Atualizar
(5) Gravar
(6) Lista Gravada
(0) Voltar para o menu principal""") 
    while True: #repetição sempre que for verdadeira
        op4 = int(input("Escolha uma opção: ")) #solicitação da escolha da opção do menu

        if op4 > 6 or op4 < 0: #so podem ser escolhido numeros de 0 a 6
            print("Opção inválida, digite novamente.")
            continue
        if op4 == 1: #opçao 1 deita para cadastro de uma nova turma
            nome_disci = pediçoes.ped_nome_disci() #pediçoes para a solicitação de dados
            cod_disci = pediçoes.ped_cod_disci()
            if disciplinas.cadastro_disci(nome_disci, cod_disci) == True: #caso seja verdadeiro mostrar que foi cadastrado
                print(" ")
                print("="*80)
                print(" ")
                print("Disciplina cadastrada com sucesso!")
                print(" ")
                menu_disci() #retrnar menu de disciplina
            else: #caso seja falso mostrar que já tem cadastro
                print(" ")
                print("="*80)
                print(" ")
                print("Disciplina já cadastrada!")
                print(" ")
                menu_disci() #retornar menu de disciplina

        elif op4 == 2: #opçao 2 feita paradeletar dados de uma turma 
            cod_disci = pediçoes.ped_cod_disci() #pediçao para a solicitaçao do codigo da disciplina
            if disciplinas.apagar_disci(cod_disci) == True: #caso o codigo da disciplina esteja na lista mostrar que foi deletado todos os dados dessa disciplina
                print(" ")
                print("="*80)
                print(" ")
                print("Disciplina deletada!")
                print(" ")
                menu_disci() #retornar menu de disciplina
            else: #caso o codigo da disciplina nao esteja na lista mstrar que nao foi encontrada
                print(" ")
                print("="*80)
                print(" ")
                print("Disciplina não encontrada!")
                print(" ")
                menu_disci() #retornar menu da disciplina

        elif op4 == 3: #opçao 3 feita para a consulta dos dados da disciplina adicionados na operaçao
            disciplinas.consultar_disci()
            menu_disci() #retornar menu da disciplina

        elif op4 == 4: #opçao 4 feita para atualizaçao dos dados da disciplina
            cod_disci = pediçoes.ped_cod_disci() #pediçao para solicitaçao do codigo da disciplina
            if disciplinas.atualizar_disci(cod_disci) == True: #caso o codigo esteja na lista mostrar que a atualizaçao foi um sucesso
                print(" ")
                print("="*80)
                print(" ")
                print("Atualização concluida com sucesso!")
                print(" ")
            menu_disci() #retornar menu da disciplina

        elif op4 == 5: #opçao 5 feita para adicionar dados da disciplina no arquivo de texto definitivo
            disciplinas.marcar_disci()
            menu_disci() #retornar menu da disciplina

        elif op4 == 6: #opçao 6 feita para mostrar dados que ja estao gravados no arquivo definitivo
            disciplinas.leitura_disci()
            menu_disci() #retornar menu da disciplina

        elif op4 == 0: #opçao 0 feita para retornar o menu principal
            menu_principal()

#MENU TURMA =======================================================================================
def menu_turma(): #funçao para menu da turma
    print("""======= MENU DA TURMA ========
(1) Adicionar
(2) Excluir
(3) Consultar
(4) Atualizar
(5) Gravar
(6) Lista Gravada
(7) Gerar Ata de Exercício
(0) Voltar para o menu principal""") 
    while True: #repetição sempre que for verdadeira
        op5 = int(input("Escolha uma opção: ")) #solicitação da escolha da opção do menu

        if op5 > 7 or op5 < 0: #só podem ser escolhidos números de 0 a 7
            print("Opção inválida, digite novamente.")
            continue
        if op5 == 1: #opção 1 feita para cadastro de uma nova turma
            cod_turma = pediçoes.ped_cod_turma() #pediçoes para a solicitação de dados
            periodo = pediçoes.ped_periodo()
            cod_disci = pediçoes.ped_cod_disci()
            cpf_prof = pediçoes.ped_cpf_prof()
            cpf_aluno = pediçoes.ped_cpf_aluno()
            if turmas.cadastro_turma(cod_turma, periodo, cod_disci, cpf_prof, cpf_aluno) == True: #caso seja verdadeiro mostrar que foi cadastrado
                print(" ")
                print("="*80)
                print(" ")
                print("Turma cadastrada com sucesso!")
                print(" ")
                menu_turma() #retornar menu de turmas
            else: #caso seja falso mostrar que já tem cadastro
                print(" ")
                print("="*80)
                print(" ")
                print("Turma já cadastrada!")
                print(" ")
                menu_turma() #retornar menu de turma

        if op5 == 2: #opção 2 feita para deletar dados de uma turma
            cod_turma = pediçoes.ped_cod_turma() #pedição para a solicitação do codigo da turma
            if turmas.apagar_turma(cod_turma) == True: #caso o codigo da turma esteja na lista mostrar que foi deletado todos os dados dessa disciplina
                print(" ")
                print("="*80)
                print(" ")
                print("Turma deletada!")
                print(" ")
                menu_turma() #retornar menu de turma
            else: #caso o codigo da turma nao esteja na lista mstrar que nao foi encontrada
                print(" ")
                print("="*80)
                print(" ")
                print("Turma não encontrada!")
                print(" ")
                menu_turma() #retornar menu de turma

        if op5 == 3: #opçao 3 feita para a consulta dos dados da turma adicionados na operaçao
            turmas.consultar_turma()
            menu_turma() #retornar menu de turma

        if op5 == 4: #opçao 4 feita para atualizaçao dos dados da turma
            cod_turma = pediçoes.ped_cod_turma() #pediçao para solicitaçao do codigo da turma
            if turmas.atualizar_turma(cod_turma) == True: #caso o codigo esteja na lista mostrar que a atualizaçao foi um sucesso
                print(" ")
                print("="*80)
                print(" ")
                print("Atualização concluida com sucesso!")
                print(" ")
            menu_turma() #retornar menu de turma

        if op5 == 5: #opçao 5 feita para adicionar dados da turma no arquivo de texto definitivo
            turmas.marcar_turma()
            menu_turma() #retornar menu de turma

        if op5 == 6: #opçao 6 feita para mostrar dados que ja estao gravados no arquivo definitivo
            turmas.leitura_turma()
            menu_turma() #retornar menu de turma
        
        if op5 == 7: #opçao 7 feita para gerar ata de exercicio
            turmas.ata()
            menu_turma() #rtornar menu de turma
            
        if op5 == 0: #opçao 0 feita para retornar o menu principal
            menu_principal()

#MENU PRINCIPAL ================================================================================
def menu_principal(): #funçao para o menu principal
    print("SISTEMA DE CONTROLE ACADÊMICO")
    print("""====== MENU PRINCIPAL =======
(1) Dados do Professor
(2) Dados do Aluno
(3) Dados da Disciplina
(4) Dados da Turma
(0) Sair""")

    while True:
        op = int(input("Escolha uma opção: \n")) #solicitação da escolha da opção do menu
        if op > 4 or op < 0: #so podem ser escolhidos numeros de 0 a 4
            print("Opção inválida, digite novamente.")
            continue

        if op == 1: #opçao 1 chama menu do professor
            menu_prof()
        if op == 2: #opçao 2 chama menu do aluno
            menu_aluno()
        if op == 3: #opçao 3 chama menu da disciplina
            menu_disci()
        if op == 4: #opçao 4 chama menu da turma 
            menu_turma()
        if op == 0: #opçao 0 fecha o programa
            break


    
