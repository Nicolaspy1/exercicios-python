informacoes = []


while True:
    nome = input("Digite o nome de usuário: ")
    if len(nome) <=  3:
        print("Nome de usuário precisa ser maior que 3 caracteres")
    else:
        informacoes.append(nome)
        break
while True:
    try:
        idade = int(input("Digite a sua idade: "))
        if idade <= 0 or idade >= 120:
            print("A idade precisa ser maior que 0 e menor que 120")
        else: 
            informacoes.append(idade)
            break
    except ValueError:
        print("Digite apenas número inteiros")  
while True:   
    try:
        salario = float(input("Digite o seu salário: "))
        if salario < 0:
            print("Salário precisa ser maior que 0")
        else:
            informacoes.append(salario)
            break
    except ValueError:
        print("Digite apenas números")

print(f"Nome: {informacoes[0]}, Idade: {informacoes[1]}, Salario: {informacoes[2]:.2f}")