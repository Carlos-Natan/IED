###############################################
# ATIVIDADE: PRATICA COM LISTA, PILHA E FILA. #
# MATÉRIA: IED / S3                           #
# DATA: 09/05/2025                            # 
# NOME: Carlos Natan Pastor de Souza          # 
###############################################


#estruturas de dados principais
tarefas = []                                                                                    #Lista principal de tarefas
historico = []                                                                                  #Pilha para desfazer tarefas
fila_execucao = []                                                                              #Fila para executar tarefas


#As funções/atribuições de cada mecanismo da interface do Usuario:
def adicionar_tarefa(nome, prioridade):                                                         #1
                                                                                                #Recebe o nome e prioridade como entrada
    tarefa = {"nome": nome, "prioridade": prioridade}                                           #Cria um dicionário com os dados da tarefa
    tarefas.append(tarefa)                                                                      #adiciona a tarefa na lista principal
    historico.append(tarefa)                                                                    #Empilha na estrutura de histórico (última tarefa no topo)
    fila_execucao.append(tarefa)                                                                #Enfileira para futura execução (ordem de chegada)
    salvar()                                                                                    #Atualiza o arquivo com as tarefas salvas
    print(f"Tarefa '{nome}' adicionada\nprioridade '{prioridade}'\n")                           #função que desfaz a última tarefa adicionada
    
    
def desfazer_ultima_tarefa():                                                                   #2
    if historico:                                                                               #Verifica se há algo na pilha (se o histórico não está vazio)
        ultima = historico.pop()                                                                #pop: Retira (e armazena) a última tarefa adicionada (topo da pilha)
        tarefas.remove(ultima)                                                                  #remove: remove a mesma tarefa da lista principal
        fila_execucao.remove(ultima)                                                            #remove da fila de execução
        salvar()                                                                                #atualiza o arquivo com o novo estado
        print(f"Tarefa '{ultima['nome']}' desfeita!\n")
    else:
        print("Nenhuma tarefa para desfazer.\n")                                                #Se a pilha está vazia, exibe aviso
        
        
#função que atende(executa)
def atender_tarefa():                                                                           #3
    if fila_execucao:                                                                           #verifica se há tarefas na fila
        feita = fila_execucao.pop(0)                                                            #rretira a primeira tarefa da fila (FIFO: índice 0)
        tarefas.remove(feita)                                                                   #remove a mesma da lista principal
        salvar()                                                                                #atualiza o arquivo
        print(f"Tarefa '{feita['nome']}' atendida!\n")                                          #avisa que foi atendida
    else:
        print("Nenhuma tarefa para atender.\n")                                                 #se a fila está vazia, mostra aviso
        
        
#exibe todas as tarefas
def mostrar_tarefas():                                                                          #4
    print("\n📋 Lista de Tarefas:")
    for i, t in enumerate(tarefas):                                                             #percorre a lista de tarefas com índice (i)
        print(f"{i + 1}. {t['nome']} | Prioridade: {t['prioridade']}")                          #exibe nome e prioridade
        print()
        
        
#função responsável por salvar as tarefas no arquivo ".txt"
def salvar():                                                                                   #5
    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:                                 #abre o arquivo para escrita
        for tarefa in tarefas:                                                                  #percorre a lista principal
            arquivo.write(f"{tarefa['nome']} | Prioridade: {tarefa['prioridade']}\n")
            
            
# interface principal (loop)
while True:
    opcao = input("\033[30;47m1.\033[0m Adicionar Tarefa\n\033[30;47m2.\033[0m Desfazer Última Tarefa\n\033[30;47m3.\033[0m Atender Tarefa (por fila)\n\033[30;47m4.\033[0mMostrar Tarefas\n\033[30;47m5.\033[0m Sair\nEscolha uma opção:\033[30;47m \033[0m")
    if opcao == '1':
        nome = input("Digite o nome da tarefa: ")
        prioridade = input("Digite a prioridade (A/B/C): ")
        adicionar_tarefa(nome, prioridade)
    elif opcao == '2':
        desfazer_ultima_tarefa()
    elif opcao == '3':
        atender_tarefa()
    elif opcao == '4':
        mostrar_tarefas()
    elif opcao == '5':
        print("Saindo do programa... ")
        break                                                                                    #encerra o programa
    else:
        print("Opção impossibilitada, tente novamente.\n")
