
def saudacao ():
    print('Bem-vindo à Academia Nara Fit! Escolha a opção desejada: ')

def calculo_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def cadastrar_idade():
    while True:
        try:
            idade = int(input('Digite a idade do aluno: '))
            break
        except ValueError:
            print('Digite apenas números inteiros')
    return idade

def cadastrar_peso():
    while True:
        try:
            peso = float(input('Digite o peso do aluno (kg): '))
            break
        except ValueError:
            print('Digite apenas números')
    return peso

def cadastrar_altura():
    while True:
        try:
            altura = float(input('Digite a altura do aluno (m): '))
            if altura > 2.10:
                print('Altura inválida. Digite apenas valores em metros (ex: 1.69)')
            else:
                break
        except ValueError:
            print('Digite apenas números e pontos (ex: 65.7)')
    return altura

def cadastrar_objetivo():
    while True:
        objetivo = input('Digite o objetivo do aluno: ').strip().title()
        if objetivo not in ['Secar', 'Ficar Grande', 'Preparo Físico', 'Preparo Fisico']:
            print('Objetivo inválido. Digite apenas Secar, Ficar Grande ou Preparo Físico')
            continue
        return objetivo

def listar_alunos():
    if len(alunos_cadastrados) == 0:
        print('Nenhum aluno cadastrado') 
    else:
        for i in alunos_cadastrados:
            print(f'Aluno {i}')


saudacao ()

alunos_cadastrados = []

while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")
    try:
        opcao = int(input("Escolha uma opcao: "))
    except ValueError:
        print('Digite uma opção válida')

    match opcao:
        case 1:
            nome = input('Digite o nome do aluno que deseja cadastrar: ').title()
            idade = cadastrar_idade()
            peso = cadastrar_peso()
            altura = cadastrar_altura()
            objetivo = cadastrar_objetivo()
            imc = calculo_imc(peso, altura)

            alunos = {
    "nome": nome,
    "idade": idade,
    "peso": peso,
    "altura": altura,
    "objetivo": objetivo,
    "imc": imc
}
            print(objetivo)
            alunos_cadastrados.append(alunos)
            
        case 2:
            listar_alunos()

        case 3:
            break
        