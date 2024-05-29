#      -----Sistema Bancário em Python-----
# Requisitos Funcionais: depósito, saque e extrato.

# Saque
# no máximo 3 saques diários, com limite máximo de 500 reais por saque;
# Se não tiver saldo, exibir mensagem: "Não foi possível realizar o saque. Saldo insuficiente!"

# Extrato
# Listar todas as movimentações, e no fim o saldo atual da conta;
# formato dos valores: R$ xxx.xx.

# Escopo
# MENU - depositar, sacar e extrato
# Salvar tudo para extrato. 

menu = """
MENU INICIAL - BANCO JVC
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Informe o que deseja realizar: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("\nInsira o valor você deseja depositar: "))
        if valor <= 0:
            print("Valor fornecido inválido.")
        else:
            print("Depositando...")
            saldo += valor
            extrato += f"Movimento de Depósito - valor de R${valor:.2f} reais.\n"
    
    elif opcao == 2:
        valor = float(input("\nInsira o valor você deseja sacar: "))
        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("Valor fornecido inválido.")
        elif valor > limite:
            print(f"Saque não realizado, seu limite é de R${limite:.2f} reais.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Não foi possível realizar o saque, limite de saque diário atingido.")
        else:
            print("Sacando...")
            saldo -= valor
            numero_saques += 1
            extrato += f"Movimento de Saque - valor de R${valor:.2f} reais.\n"

    elif opcao == 3:
        print("\nGerando Extrato: ")
        print("Extrato sem movimento." if not extrato else extrato)
        print(f"Saldo atual: R${saldo:.2f} reais.\n")
    
    elif opcao == 4:
        print("O Banco JVC agradece pela sua visita. Volte sempre!\n")
        break
    
    else:
        print("Operação invalida, por favor selecione novamente uma operação desejada.")