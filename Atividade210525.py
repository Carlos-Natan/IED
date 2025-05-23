pilha = []
fila = []

while True:
    p1 = input("Informe a posição do usuário: ")
    pilha.append(p1)

    o = input("\n0. Sair\n1. Informar dados\n2. Mostrar dados\n3. Marcar ordem de chegada\nEscolha uma opção: ")
    
    if o == "1":
        n = input("Nome: ")
        c = input("Cidade: ")
        t = input("Trabalho: ")
        
        usuario = {
            "NOME": n,
            "CIDADE": c,
            "TRABALHO": t,
            "POSICAO": p1
        }
        fila.append(usuario)
        
    elif o == "2":
        print("\nUSUÁRIOS CADASTRADOS: ")
        for u in fila:
            print(u)
        print("\nORDEM DE CHEGADA (PILHA): ")
        print(pilha)
        
    elif o == "0":
        print("Saindo...")
        break
        
    else:
        print("\n\033[31;47m\ainvalido\033[0m\n")
