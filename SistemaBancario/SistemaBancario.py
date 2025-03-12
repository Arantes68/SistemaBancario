# MENU INICIAL: É USADO O """ PARA FAZER A PERSONALIZAÇÃO PARA APARECER AO USUÁRIO.
menu = """ 

========================================================
                      BANCO DIGITAL
========================================================

Escolha uma das opções abaixo:

[1] Depositar
[2] Saque
[3] Extrato
[4] Sair



Por gentileza, insira a opção desejada: 
"""

# VARIÁVEIS.
saldo = 0  #Variável que irá armazenar int
limite = 500
extrato = ""  #Variável que irá armazenar string
numero_saques = 0
LIMITE_SAQUES = 3  #Variável Constante

# O PROGRAMA CONTINUARÁ EXECUTANDO ATÉ QUE O USUÁRIO ESCOLHA A OPÇÃO DE SAIR (OPÇÃO 4).
while True:
     
    # Exibe o menu e solicita ao usuário que insira o número correspondente à operação desejada
    opcao = input(menu)  # Captura a entrada do usuário

    # DEPOSITAR
    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    # SACAR
    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        
        #Condições
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    # EXTRATO
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato) # not extrato: Se a condição for verdadeira, retorna a mensagem.
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # SAIR DO LOOP; ENCERRANDO A EXECUÇÃO.
    elif opcao == 4:
        print("Saindo... Até logo!")
        break

    # SE O USUÁRIO DIGITAR ALGUMA OPÇÃO QUE NÃO ESTÁ NO MENU, ELE INFORMA QUE A OPERAÇÃO É INVÁLIDA.
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
