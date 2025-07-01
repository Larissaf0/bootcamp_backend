# 👇 Dados iniciais
saldo = 0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500

# 👋 Menu
menu = '''\n===== Banking System =====
0 - Depósito
1 - Extrato
2 - Saque
3 - Saldo
4 - Encerrar
========================'''

# 💸 Função depósito
def deposito(saldo, extrato):
    valor = float(input('Digite o valor a ser depositado: R$ '))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito de R$ {valor:.2f}")
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("❌ Valor inválido!")
    return saldo, extrato

# 💰 Função saque com limites
def saque(saldo, extrato, numero_saques, LIMITE_SAQUES, LIMITE_VALOR_SAQUE):
    if numero_saques >= LIMITE_SAQUES:
        print("🚫 Limite diário de 3 saques atingido.")
        return saldo, extrato, numero_saques

    valor = float(input("Informe o valor do saque: R$ "))

    if valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > LIMITE_VALOR_SAQUE:
        print(f"❌ Saques acima de R$ {LIMITE_VALOR_SAQUE:.2f} não são permitidos.")
    elif valor <= 0:
        print("❌ Valor inválido.")
    else:
        saldo -= valor
        extrato.append(f"Saque de R$ {valor:.2f}")
        numero_saques += 1
        print("✅ Saque realizado com sucesso!")

    return saldo, extrato, numero_saques

# 📄 Função extrato
def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=============================\n")

# 🔁 Loop principal
while True:
    print(menu)
    opcao = input("Escolha a opção: ")

    if opcao == "0":
        saldo, extrato = deposito(saldo, extrato)
    elif opcao == "1":
        exibir_extrato(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, numero_saques = saque(saldo, extrato, numero_saques, LIMITE_SAQUES, LIMITE_VALOR_SAQUE)
    elif opcao == "3":
        print(f"💰 Saldo atual: R$ {saldo:.2f}")
    elif opcao == "4":
        print("👋 Saindo do sistema. Obrigado por usar o banco!")
        break
    else:
        print("❌ Opção inválida. Tente novamente.")
