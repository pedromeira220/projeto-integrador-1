print("Bem-vindo ao seu sistema de sustentabilidade pessoal!")
print("O sistema classificará o seu nível de sustentabilidade diário com base no seu consumo de recursos.")
print("Você digitará o dia e a média de consumo de recursos e o sistema exibirá a classificação.")

digitou_corretamente = False
ano = 0
mes = 0
dia = 0
litros_de_agua = 0

ANO_ATUAL = 2025  # TODO: colocar o ano atual automaticamente

print("Digite a data, começando pelo ano.")

# TODO: avaliar se vamos deixar colocar dados históricos.

while not digitou_corretamente:
    try:
        ano = int(input("Qual o ano? "))
    except ValueError:  # se der erro...
        print("O ano deve ser um inteiro; tente novamente!")
    else:  # senão, ou seja, se não der erro...
        if ano < 2000 or ano > ANO_ATUAL:  # ano fora da faixa válida
            print("O ano deve estar entre 2000 e 2025!")
        else:  # o ano está na faixa válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        mes = int(input("Qual o mês? "))
    except ValueError:  # se der erro...
        print("O mês deve ser um inteiro; tente novamente!")
    else:  # senão, ou seja, se não der erro...
        if mes < 1 or mes > 12:  # mês fora da faixa válida
            print("O mês deve estar entre 1 e 12!")
        else:  # o mês está na faixa válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        dia = int(input("Qual o dia? "))
    except ValueError:  # se der erro...
        print("O dia deve ser um inteiro; tente novamente!")
    else:  # senão, ou seja, se não der erro...
        if dia < 1 or dia > 31:  # dia fora da faixa válida
            print("O dia deve estar entre 1 e 31!")
        else:  # o dia está na faixa válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        litros_de_agua = float(input("Quantos litros de água aproximadamente você utilizou hoje? "))
    except ValueError:  # se der erro...
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else:  # senão, ou seja, se não der erro...
        if litros_de_agua < 0:  # valor negativo não é válido
            print("A quantidade não pode ser negativa!")
        else:  # a quantidade de água é válida
            digitou_corretamente = True

digitou_corretamente = False

# Aqui você pode adicionar outros campos para obter mais informações.
