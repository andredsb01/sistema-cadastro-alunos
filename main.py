nome = []
idade = []
nota = []

def pop():
    nome = input("Digite o nome do aluno: ").lower().title()
    return nome

def add_aluno():
    

    a = pop()
    b = int(input("Digite a idade do aluno: "))
    while(True):
        c = int(input("Digite a nota do aluno: "))  
        if c > 10 or c < 0:
            print("A nota deve estar entre 0 e 10. DIGITE NOVAMENTE")
        else: break
            
    
    global nome
    global idade
    global nota
    nome.append(a)
    idade.append(b)
    nota.append(c)
    
    return

def buscar_aluno(name):
    global nome
    x = nome.index(name)
    if x != -1:
        return x

def remover_aluno(name):
    
    x = buscar_aluno(name)
    alunos["aluno"].pop(x)
    alunos["idade"].pop(x)
    alunos["nota"].pop(x)
        
    return

def media():
    global nota
    media = 0
    elementos = 0
    
    for nota in nota:
        media += nota
        elementos += 1
    
    return media / elementos

alunos = {
    "aluno" : nome,
    "idade" : idade,
    "nota" : nota
}

while(True):
    entrada = int(input("""
1. Adicionar aluno
2. Listar todos os alunos
3. Buscar aluno pelo nome
4. Remover aluno
5. Mostrar média geral das notas
6. Sair
"""))
    
    
    match entrada:
        case 1:
            if add_aluno():
                print("Aluno cadastrado")
        case 2:
            if alunos["aluno"] == []:
                print('Não ah, nenhum aluno cadastrado.')
            else:
                for a, i, n in zip(alunos["aluno"], alunos["idade"], alunos["nota"]):
                    print(f"""Aluno: {a}, {i} Anos, Nota {n}""")
        
        case 3:
            name = pop()
            try:
                x = buscar_aluno(name)
                print(f"Aluno: {alunos[["aluno"][x]][-1]} \nIdade: {alunos[["idade"][x]][-1]} \nNota: {alunos[["nota"][x]][-1]}")
                
            except Exception as e:
                print(e)
            
            
        case 4:
            name = pop()
            try:
                remover_aluno(name)
                print(f"Aluno {name} removido.")
            except Exception as e:
                print(e)
            
        case 5:
            try:
                print(f"A média geral é de: {media()}")
            except Exception as e:
                print(e)
            
        case 6:
            print("VOCÊ ESCOLHEU SAIR...")
            break
        case _:
            print("OPÇÃO INVALIDA TENTE NOVAMENTE")
            continue