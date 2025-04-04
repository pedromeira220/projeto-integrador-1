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

# TODO: criar validação para dias do mês (não permitir 30 de fevereiro, ano bissexto ou coisa do tipo)

def ano_bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

def dias_no_mes(mes, ano):
    meses_com_31 = [1, 3, 5, 7, 8, 10, 12]
    meses_com_30 = [4, 6, 9, 11]
    
    if mes in meses_com_31:
        return 31
    elif mes in meses_com_30:
        return 30
    elif mes == 2:
        if(ano_bissexto(ano)):
            return 29
        else:
            return 28
    else:
        return 0 # erro

while not digitou_corretamente:
    try:
        ano = int(input("Qual o ano? "))
    except ValueError:  
        print("O ano deve ser um inteiro; tente novamente!")
    else: 
        if ano < 2000 or ano > ANO_ATUAL:  # ano fora da faixa válida
            print("O ano deve estar entre 2000 e 2025!")
        else:  # o ano está na faixa válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        mes = int(input("Qual o mês? "))
    except ValueError:  
        print("O mês deve ser um inteiro; tente novamente!")
    else: 
        if mes < 1 or mes > 12:  # mês fora da faixa válida
            print("O mês deve estar entre 1 e 12!")
        else:  # o mês está na faixa válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        dia = int(input("Qual o dia? "))
        if dia < 1 or dia > dias_no_mes(mes, ano): 
            print(f"O mês {mes} no ano {ano} tem apenas {dias_no_mes(mes, ano)} dias! Tente novamente.")
        else:
            digitou_corretamente = True
    except ValueError:  
        print("O dia deve ser um inteiro; tente novamente!")

digitou_corretamente = False

while not digitou_corretamente:
    try:
        consumo_litros_de_agua = float(input("Quantos litros de água aproximadamente você utilizou hoje? "))
    except ValueError:  
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else: 
        if consumo_litros_de_agua < 0:  # valor negativo não é válido
            print("A quantidade não pode ser negativa!")
        else:  # a quantidade de água é válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        consumo_energia = float(input("Quantos kWh de energia elétrica aproximadamente você utilizou hoje? "))
    except ValueError:  
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else: 
        if consumo_energia < 0:  # valor negativo não é válido
            print("A quantidade não pode ser negativa!")
        else:  # a quantidade de energia é válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        lixo_gerado = float(input("Quantos Kg de resíduos não reciclaveís você gerou hoje? "))
    except ValueError:  
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else: 
        if lixo_gerado < 0:  # valor negativo não é válido
            print("A quantidade não pode ser negativa!")
        else:  # a quantidade de residuo é válida
            digitou_corretamente = True

digitou_corretamente = False

while not digitou_corretamente:
    try:
        lixo_reciclavel = int(input("Qual a porcentagem de resíduos reciclados no total (em %)? "))
    except ValueError:  
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else: 
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
        meio_de_transporte = int(input("Qual o meio de transporte você mais usou hoje? ")) # o usuário poderá escolher apenas um meio de transporte
    except ValueError:  
        print("A quantidade deve ser um valor numérico; tente novamente!")
    else: 
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
elif lixo_reciclavel < 50 and lixo_reciclavel > 10:
    print("Média sustentabilidade")
else:
    print("Baixa sustentabilidade")

print("Classificação de uso de transporte:")
if meio_de_transporte == 1 or meio_de_transporte == 2 or meio_de_transporte == 3:
    print("Alta sustentabilidade")
elif meio_de_transporte == 4:   
    print("Média sustentabilidade")
else:
    print("Baixa sustentabilidade")
    
print("\nFim do programa")