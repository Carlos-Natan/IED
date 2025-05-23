pilha = []
fila = []

while True:
    p1 = input("informe a posiçao do usuario: ")
    pilha.append(p1)

    o = input("\n0. sair\n1. informar dados\n2. mostrar dados\n3. marcar ordem de chegada\nescolha uma opcao: ")
    
    if o == "1":
        n = input("NOME: ")
        c = input("CIDADE: ")
        t = input("TRABALHO: ")
        
        usuario = {
            "NOME": n,
            "CIDADE": c,
            "TRABALHO": t,
            "POSICAO": p1
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
        print("\n\033[31;47m\ainvalido\033[0m\n")
