alunos = []  

def cadastrar_aluno():
    print("\n=== CADASTRAR ALUNO ===")
    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")

    aluno = {"nome": nome, "idade": idade, "curso": curso}
    alunos.append(aluno)
    print(" Aluno cadastrado com sucesso!\n")

def listar_alunos():
    print("\n=== LISTA DE ALUNOS ===")
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.\n")
        return

    for i, aluno in enumerate(alunos):
        print(f"{i + 1}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
    print()

def atualizar_aluno():
    print("\n=== ATUALIZAR ALUNO ===")
    listar_alunos()
    if len(alunos) == 0:
        return

    try:
        indice = int(input("Digite o número do aluno para atualizar: ")) - 1
        if 0 <= indice < len(alunos):
            nome = input("Novo nome (deixe vazio para manter): ")
            idade = input("Nova idade (deixe vazio para manter): ")
            curso = input("Novo curso (deixe vazio para manter): ")

            if nome:
                alunos[indice]["nome"] = nome
            if idade:
                alunos[indice]["idade"] = idade
            if curso:
                alunos[indice]["curso"] = curso

            print(" Aluno atualizado com sucesso!\n")
        else:
            print(" Número inválido!\n")
    except ValueError:
        print(" Digite um número válido!\n")

def excluir_aluno():
    print("\n=== EXCLUIR ALUNO ===")
    listar_alunos()
    if len(alunos) == 0:
        return

    try:
        indice = int(input("Digite o número do aluno para excluir: ")) - 1
        if 0 <= indice < len(alunos):
            aluno_removido = alunos.pop(indice)
            print(f" Aluno {aluno_removido['nome']} removido com sucesso!\n")
        else:
            print(" Número inválido!\n")
    except ValueError:
        print(" Digite um número válido!\n")

def menu():
    while True:
        print("===== MENU CRUD ALUNOS =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Atualizar aluno")
        print("4 - Excluir aluno")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            excluir_aluno()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print(" Opção inválida!\n")

# Executar o menu
menu()