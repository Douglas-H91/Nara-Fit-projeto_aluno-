alunos_cadastrados = {
    "nome": [],
    "idade": [],
    "peso": [],
    "altura": [],
    "imc": [],
    "objetivo": []
} 
print('Bem-vindo à Academia Nara Fit! Digite a opção desejada')

while True:

    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        nome = input('Digite o nome do aluno que deseja cadastrar: ').title()
        idade = int(input('Digite a idade do aluno: '))
        peso = float(input('Digite o peso do aluno (kg): '))
        altura = float(input('Digite a altura do aluno (m): '))
        objetivo = input('Digite o objetivo do aluno: ').title()

        alunos_cadastrados["nome"].append(nome)
        alunos_cadastrados["idade"].append(idade)
        alunos_cadastrados["peso"].append(peso)
        alunos_cadastrados["altura"].append(altura)
        alunos_cadastrados["imc"].append(peso / (altura ** 2))
        alunos_cadastrados["objetivo"].append(objetivo)
    elif opcao == 2:
        if len(alunos_cadastrados) == 0:
            print('Nenhum aluno cadastrado') 
        else:
            for i in alunos_cadastrados:
                print(f'Aluno {i}')
    elif opcao == 3:
        break
    else:
        print('Escolha uma opção válida')