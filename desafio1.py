# Primeiro projeto de estudo de Python

# Desenvolvendo um sistema bancário

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d": # Depósito
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na operação: O valor informado é inválido.")
    
    elif opcao == "s": #Saque
        valor = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação: Saldo insuficiente!")

        elif excedeu_limite:
            print("Falha na operação: Limite não disponível!")

        elif excedeu_saques:
            print("Falha na operação: Número total de saques excedido.")

        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Falha na operação: O valor informado é inválido.")

    elif opcao == "e": #Extrato
        print("\n################ EXTRATO ################")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###########################################")

    elif opcao == "q": #Sair
        break

    else:
        print("Falha na operação: O valor informado é inválido.")