import mysql.connector

conexao = mysql.connector.connect(
    host="172.16.12.14",
    user="BD240225247",
    password="Ioskd9",
    database="BD240225247"
)
cursor = conexao.cursor()

ANO_ATUAL = 2025 

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
        if ano_bissexto(ano):
            return 29
        else:
            return 28
    else:
        return 0

def validar_data():
    while True:
        try:
            ano = int(input("Qual o ano? "))
            if ano < 2000 or ano > ANO_ATUAL:
                print("\033[91mO ano deve estar entre 2000 e 2025!\033[m")
                continue
            mes = int(input("Qual o mês? "))
            if mes < 1 or mes > 12:
                print("\033[91mO mês deve estar entre 1 e 12!\033[m")
                continue
            dia = int(input("Qual o dia? "))
            if dia < 1 or dia > dias_no_mes(mes, ano):
                print(f"\033[91mO mês {mes} no ano {ano} tem apenas {dias_no_mes(mes, ano)} dias!\033[m")
                continue
            return f"{ano}-{mes:02d}-{dia:02d}"
        except ValueError:
            print("\033[91mValor inválido, tente novamente!\033[m")

def ler_float(mensagem, minimo=None, maximo=None, permitir_zero=False):
    while True:
        try:
            valor = float(input(mensagem))
            if (minimo is not None and (valor < minimo or (valor == 0 and not permitir_zero))):
                print(f"\033[91mValor deve ser maior que {minimo}!\033[m")
            elif maximo is not None and valor > maximo:
                print(f"\033[91mValor deve ser menor ou igual a {maximo}!\033[m")
            else:
                return valor
        except ValueError:
            print("\033[91mValor inválido, tente novamente!\033[m")

def ler_int(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"\033[91mValor deve estar entre {minimo} e {maximo}!\033[m")
            else:
                return valor
        except ValueError:
            print("\033[91mValor inválido, tente novamente!\033[m")

def cadastrar_parametros():
    print("\nCadastro de parâmetros diários de sustentabilidade:")
    data = validar_data()
    consumo_agua = ler_float("Quantos litros de água aproximadamente você utilizou hoje? ", minimo=0.01, maximo=1000000)
    consumo_energia = ler_int("Quantos kWh de energia elétrica aproximadamente você utilizou hoje? ", minimo=1, maximo=10000)
    residuos_nao_reciclaveis = ler_float("Quantos Kg de resíduos não recicláveis você gerou hoje? ", minimo=0.01, maximo=1000)
    percentual_reciclado = ler_float("Qual a porcentagem de resíduos reciclados no total (em %)? ", minimo=0.01, maximo=100)
    print('Meio de transporte:\n1. Transporte público (Ônibus, metrô, trem).\n2. Bicicleta.\n3. Caminhada.\n4. Carro (combustível fósseis).\n5. Carro elétrico.\n6. Carona compartilhada.')
    meio_transporte = ler_int("Qual o meio de transporte você mais usou hoje dos listados acima? ", 1, 6)

    query = """
    INSERT INTO registros_sustentabilidade (
        data_registro, consumo_agua_litros, consumo_energia_kwh,
        residuos_nao_reciclaveis_kg, percentual_reciclado, meio_transporte_codigo
    ) VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (data, consumo_agua, consumo_energia, residuos_nao_reciclaveis, percentual_reciclado, meio_transporte)
    cursor.execute(query, valores)
    conexao.commit()
    print("\033[92mCadastro realizado com sucesso!\033[m")

def listar_registros():
    cursor.execute("SELECT * FROM registros_sustentabilidade ORDER BY data_registro")
    registros = cursor.fetchall()
    if not registros:
        print("\033[93mNenhum registro encontrado.\033[m")
        return []

    print("\nLista de registros cadastrados:\n")
    print(f"{'Id'}   {'Data'}               {'Água (L)'}     {'Energia (kWh)'} {'% Reciclado'} {'Transporte'}")
    for reg in registros:
        idr, data_registro, consumo_agua_litros, consumo_energia_kwh, residuos_nao_reciclaveis, percentual_reciclado, meio_transporte = reg
        print(f"{idr:<4} {data_registro} {consumo_agua_litros:<10} {consumo_energia_kwh:<14} {residuos_nao_reciclaveis:<17} {percentual_reciclado:<12} {meio_transporte:<10}")
    return registros

def alterar_parametros():
    print("\nAlteração de parâmetros diários de sustentabilidade:")
    registros = listar_registros()
    if not registros:
        return
    id_alterar = ler_int("Digite o Id do registro que deseja alterar: ")
    cursor.execute("SELECT * FROM registros_sustentabilidade WHERE id_registro = %s", (id_alterar,))
    registro = cursor.fetchone()
    if not registro:
        print("\033[91mRegistro não encontrado!\033[m")
        return

    print("Digite os novos dados (aperte Enter para manter o valor atual):")

    while True:
        nova_data = input(f"Data atual ({registro[1]}): ")
        if nova_data.strip() == '':
            data = registro[1]
            break
        else:
            try:
                ano, mes, dia = map(int, nova_data.split('-'))
                if ano < 2000 or ano > ANO_ATUAL:
                    print("\033[91mAno inválido.\033[m")
                    continue
                if mes < 1 or mes > 12:
                    print("\033[91mMês inválido.\033[m")
                    continue
                if dia < 1 or dia > dias_no_mes(mes, ano):
                    print("\033[91mDia inválido para o mês e ano informados.\033[m")
                    continue
                data = nova_data
                break
            except:
                print("\033[91mFormato inválido. Use AAAA-MM-DD.\033[m")

    def ler_float_opcional(mensagem, valor_atual, minimo=None, maximo=None):
        while True:
            entrada = input(f"{mensagem} (atual {valor_atual}): ")
            if entrada.strip() == '':
                return valor_atual
            try:
                valor = float(entrada)
                if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                    print(f"\033[91mValor deve estar entre {minimo} e {maximo}.\033[m")
                    continue
                return valor
            except:
                print("\033[91mValor inválido.\033[m")

    def ler_int_opcional(mensagem, valor_atual, minimo=None, maximo=None):
        while True:
            entrada = input(f"{mensagem} (atual {valor_atual}): ")
            if entrada.strip() == '':
                return valor_atual
            try:
                valor = int(entrada)
                if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                    print(f"\033[91mValor deve estar entre {minimo} e {maximo}.\033[m")
                    continue
                return valor
            except:
                print("\033[91mValor inválido.\033[m")

    consumo_agua = ler_float_opcional("Consumo de água (L)", registro[2], 0.01, 1000000)
    consumo_energia = ler_int_opcional("Consumo de energia (kWh)", registro[3], 1, 10000)
    residuos = ler_float_opcional("Resíduos não recicláveis (Kg)", registro[4], 0.01, 1000)
    reciclado = ler_float_opcional("Percentual reciclado (%)", registro[5], 0.01, 100)
    print('Meio de transporte:\n1. Transporte público (Ônibus, metrô, trem).\n2. Bicicleta.\n3. Caminhada.\n4. Carro (combustível fósseis).\n5. Carro elétrico.\n6. Carona compartilhada.')
    meio_transporte = ler_int_opcional("Meio de transporte", registro[6], 1, 6)

    query = """
    UPDATE registros_sustentabilidade SET
    data_registro=%s, consumo_agua_litros=%s, consumo_energia_kwh=%s,
    residuos_nao_reciclaveis_kg=%s, percentual_reciclado=%s, meio_transporte_codigo=%s
    WHERE id_registro=%s
    """
    valores = (data, consumo_agua, consumo_energia, residuos, reciclado, meio_transporte, id_alterar)
    cursor.execute(query, valores)
    conexao.commit()
    print("\033[92mRegistro alterado com sucesso!\033[m")

def excluir_parametros():
    print("\nExclusão de parâmetros diários de sustentabilidade:")
    registros = listar_registros()
    if not registros:
        return
    id_excluir = ler_int("Digite o ID do registro que deseja excluir: ")
    cursor.execute("SELECT * FROM registros_sustentabilidade WHERE id_registro = %s", (id_excluir,))
    registro = cursor.fetchone()
    if not registro:
        print("\033[91mRegistro não encontrado!\033[m")
        return

    confirma = input(f"Confirma exclusão do registro {id_excluir} (s/n)? ").lower()
    if confirma == 's':
        cursor.execute("DELETE FROM registros_sustentabilidade WHERE id_registro = %s", (id_excluir,))
        conexao.commit()
        print("\033[92mRegistro excluído com sucesso!\033[m")
    else:
        print("Exclusão cancelada.")

def classificar_parametros():
    print("\nClassificação de sustentabilidade dos registros:")
    registros = listar_registros()
    if not registros:
        return

    print("\nClassificações:")
    for reg in registros:
        idr, data, agua, energia, residuos, reciclado, transporte = reg
        print(f"\nID {idr} - Data {data}")
        print("  Água: ", end='')
        if agua < 150:
            print("\033[92mAlta sustentabilidade.\033[m")
        elif agua < 200:
            print("\033[93mMédia sustentabilidade.\033[m")
        else:
            print("\033[91mBaixa sustentabilidade.\033[m")

        print("  Energia: ", end='')
        if energia < 5:
            print("\033[92mAlta sustentabilidade.\033[m")
        elif energia < 10:
            print("\033[93mMédia sustentabilidade.\033[m")
        else:
            print("\033[91mBaixa sustentabilidade.\033[m")

        print("  Resíduos não recicláveis: ", end='')
        if residuos < 5:
            print("\033[92mAlta sustentabilidade.\033[m")
        elif residuos < 10:
            print("\033[93mMédia sustentabilidade.\033[m")
        else:
            print("\033[91mBaixa sustentabilidade.\033[m")

        print("  Percentual reciclado: ", end='')
        if reciclado > 50:
            print("\033[92mAlta sustentabilidade.\033[m")
        elif reciclado > 10:
            print("\033[93mMédia sustentabilidade.\033[m")
        else:
            print("\033[91mBaixa sustentabilidade.\033[m")

        print("  Transporte: ", end='')
        if transporte in [1, 2, 3]:
            print("\033[92mAlta sustentabilidade.\033[m")
        elif transporte == 4:
            print("\033[93mMédia sustentabilidade.\033[m")
        else:
            print("\033[91mBaixa sustentabilidade.\033[m")

    # Média dos parâmetros
    cursor.execute("""
    SELECT 
        ROUND(AVG(consumo_agua_litros),2),
        ROUND(AVG(consumo_energia_kwh),2),
        ROUND(AVG(residuos_nao_reciclaveis_kg),2),
        ROUND(AVG(percentual_reciclado),2)
    FROM registros_sustentabilidade;
    """)
    medias = cursor.fetchone()
    if medias[0] is None:
        print("\n\033[93mSem dados para cálculo das médias.\033[m")
        return

    print("\n\033[94mMédias gerais dos parâmetros:\033[m")
    print(f"Média de água (L): {medias[0]}")
    print(f"Média de energia (kWh): {medias[1]}")
    print(f"Média de resíduos não recicláveis (Kg): {medias[2]}")
    print(f"Média de reciclado (%): {medias[3]}")

    print("\nClassificação geral baseada nas médias:")
    print("  Água: ", end='')
    if medias[0] < 150:
        print("\033[92mAlta sustentabilidade.\033[m")
    elif medias[0] < 200:
        print("\033[93mMédia sustentabilidade.\033[m")
    else:
        print("\033[91mBaixa sustentabilidade.\033[m")

    print("  Energia: ", end='')
    if medias[1] < 5:
        print("\033[92mAlta sustentabilidade.\033[m")
    elif medias[1] < 10:
        print("\033[93mMédia sustentabilidade.\033[m")
    else:
        print("\033[91mBaixa sustentabilidade.\033[m")

    print("  Resíduos não recicláveis: ", end='')
    if medias[2] < 5:
        print("\033[92mAlta sustentabilidade.\033[m")
    elif medias[2] < 10:
        print("\033[93mMédia sustentabilidade.\033[m")
    else:
        print("\033[91mBaixa sustentabilidade.\033[m")

    print("  Percentual reciclado: ", end='')
    if medias[3] > 50:
        print("\033[92mAlta sustentabilidade.\033[m")
    elif medias[3] > 10:
        print("\033[93mMédia sustentabilidade.\033[m")
    else:
        print("\033[91mBaixa sustentabilidade.\033[m")

def menu():
    while True:
        print("\n\033[94mSistema de Monitoramento de Sustentabilidade Pessoal\033[m")
        print("1 - Cadastro de parâmetros diários")
        print("2 - Alteração de parâmetros diários")
        print("3 - Exclusão de parâmetros diários")
        print("4 - Classificação e listagem de sustentabilidade")
        print("5 - Sair do sistema")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_parametros()
        elif escolha == '2':
            alterar_parametros()
        elif escolha == '3':
            excluir_parametros()
        elif escolha == '4':
            classificar_parametros()
        elif escolha == '5':
            print("Saindo do sistema.")
            break
        else:
            print("\033[91mOpção inválida. Tente novamente.\033[m")

print("\033[094mBem-vindo ao seu sistema de sustentabilidade pessoal!\033[m")
menu()
cursor.close()
conexao.close()
