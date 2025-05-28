pilha = []
fila = []

while True:
    p1 = input("\033[01;3mINFORME A SUA POSICAO: ")
    pilha.append(p1)

    o = input("\n0. Sair\n1. Informar dados\n2. Mostrar dados\n3. Marcar ordem de chegada\nEscolha uma opção: ")
    
    if o == "1":
        n = input("NOME: ")
        c = input("CIDADE: ")
        t = input("TRABALHO: ")
        tr = input("ACECO A TRANSPORTE (\033[0m\033[32mSIM\033[0m/\033[31mNÃO\033[0m\033[01m): ")
        
        if tr == "SIM":
            ti = input("TIPO DE TRANSPORTE: ")
            
        else:
            ti = input("JUSTIFIQUE: ")
        
        usuario = {
            "NOME:": n,
            "CIDADE:": c,
            "TRABALHO:": t,
            "TRANSPORTE:": tr,
            "DT:": ti, #Dados de Transporte
            "POSICAO:": p1
        }
        fila.append(usuario)
        
    elif o == "2":
        print("\nUSUARIOS CADASTRADOS: ")
        for u in fila:
            print(u)
        print("\nORDEM DE CHEGADA EM PILHA: ")
        print(pilha)
        
    elif o == "0":
        print("SAINDO...")
        break
        
    else:
        print("\n\033[31;4m\aINAVALIDO.\033[0m\n")
