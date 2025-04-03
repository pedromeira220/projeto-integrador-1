print("Bem-vindo ao seu sistema de sustentabilidade pessoal!")
print("O sistema classificará o seu nível de sustentabilidade diário com base no seu consumo de recursos.")
print("Você digitará o dia e a média de consumo de recursos e o sistema exibirá a classificação.")

digitou_corretamente = False
ano = 0
mes = 0
dia = 0
consumo_litros_de_agua = 0

ANO_ATUAL = 2025  # TODO: colocar o ano atual automaticamente

print("Digite a data, começando pelo ano.")

# TODO: avaliar se vamos deixar colocar dados muito no passado
# TODO: criar validação para dias do mês (não permitir 30 de fevereiro, ano bissexto ou coisa do tipo)

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
        consumo_litros_de_agua = float(input("Quantos litros de água aproximadamente você utilizou hoje? "))
    except ValueError:  # se der erro...
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else:  # senão, ou seja, se não der erro...
        if consumo_litros_de_agua < 0:  # valor negativo não é válido
            print("A quantidade não pode ser negativa!")
        else:  # a quantidade de água é válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        consumo_energia = float(input("Quantos kWh de energia elétrica aproximadamente você utilizou hoje? "))
    except ValueError:  # se der erro...
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else:  # senão, ou seja, se não der erro...
        if consumo_energia < 0:  # valor negativo não é válido
            print("A quantidade não pode ser negativa!")
        else:  # a quantidade de energia é válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        lixo_gerado = float(input("Quantos Kg de resíduos não reciclaveís você gerou hoje? "))
    except ValueError:  # se der erro...
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else:  # senão, ou seja, se não der erro...
        if lixo_gerado < 0:  # valor negativo não é válido
            print("A quantidade não pode ser negativa!")
        else:  # a quantidade de residuo é válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        lixo_reciclavel = int(input("Qual a porcentagem de resíduos reciclados no total (em %)? "))
    except ValueError:  # se der erro...
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else:  # senão, ou seja, se não der erro...
        if lixo_reciclavel < 0:  # valor negativo não é válido
            print("A quantidade não pode ser negativa!")
        else:  # a quantidade de residuos reciclados é válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        print('1. Transporte público (Ônibus, metrô, trem).\n'
                '2. Bicicleta.\n'
                '3. Caminhada.\n'
                '4. Carro (combustivel fósseis).\n'
                '5. Carro elétrico.\n'
                '6. Carona compartilhada.')
        meio_de_transporte = int(input("Qual o meio de transporte você usou hoje? "))
    except ValueError:  # se der erro...
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else:  # senão, ou seja, se não der erro...
        if meio_de_transporte < 1 or meio_de_transporte > 6:  # valores fora da faixa dão erro
            print("A quantidade tem de ser entre 1 e 6")
        else:  # o meio de transporte escolhido é válida
            digitou_corretamente = True

digitou_corretamente = False

print("\nClassificação de sustentabilidade: \n")

print("Classificação de água:")
if consumo_litros_de_agua < 150:
    print("Alta sustentabilidade")
elif consumo_litros_de_agua >= 150 and consumo_litros_de_agua < 200:
    print("Média sustentabilidade")
else:
    print("Baixa sustentabilidade")

print("Classificação de energia elétrica:")
if consumo_energia < 5:
    print("Alta sustentabilidade")
elif consumo_energia >= 5 and consumo_energia < 10:
    print("Média sustentabilidade")
else:
    print("Baixa sustentabilidade")

print("Classificação de resíduos não reciclaveis:")
if lixo_reciclavel > 50:
    print("Alta sustentabilidade")
elif lixo_reciclavel <50 and lixo_reciclavel > 10:
    print("Média sustentabilidade")
else:
    print("Baixa sustentabilidade")

print("Classificação de uso de transporte:")
if meio_de_transporte ==2 or meio_de_transporte == 3 or meio_de_transporte == 5:
    print("Alta sustentabilidade")
elif meio_de_transporte == 1 or meio_de_transporte == 6:
    print("Média sustentabilidade")
else:
    print("Baixa sustentabilidade")
    
print("\nFim do programa")