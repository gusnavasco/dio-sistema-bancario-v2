menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar novo usuario
[m] Mostrar usuarios
[c] Criar nova conta corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []

contas = []
numero_conta = 1
numero_agencia = "0001"


def depositar(saldo, extrato,/):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return (saldo, extrato)


def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

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
    
    return (saldo, extrato, numero_saques)


def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = ""
    cpf_bruto = input("CPF: ")
    for caractere in cpf_bruto:
        if caractere.isdecimal():
            cpf += caractere
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuario ja existe\n")
            return None
    nome = input("Nome do usuario: ")
    data_de_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereco (Logradouro, Nro - Bairro - Cidade/Sigla estado): ")
    return {"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco}


def criar_conta_corrente(usuarios, numero_conta, numero_agencia=numero_agencia):
    cpf = ""
    cpf_bruto = input("A conta sera vinculada a qual CPF? CPF: ")
    for caractere in cpf_bruto:
        if caractere.isdecimal():
            cpf += caractere
    
    usuario_da_conta = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_da_conta = usuario
    if usuario_da_conta:
        conta_corrente = {"agencia": numero_agencia, "numero da conta": numero_conta, "usuario": usuario_da_conta}
        numero_conta += 1
        return (numero_conta, conta_corrente)
    else:
        print("CPF nao cadastrado.")
        return (numero_conta, None)    


def mostrar_usuarios(usuarios):
    print("\nUsuarios: ")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}\n")


while True:

    opcao = input(menu)

    if opcao == "d":
        (saldo, extrato) = depositar(saldo, extrato)

    elif opcao == "s":
        (saldo, extrato, numero_saques) = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)
    
    elif opcao == "u":
        novo_usuario = criar_usuario(usuarios)
        if novo_usuario:
            usuarios.append(novo_usuario)

    elif opcao == "m":
        mostrar_usuarios(usuarios)

    elif opcao == "c":
        (numero_conta, nova_conta_corrente) = criar_conta_corrente(usuarios, numero_conta)
        if nova_conta_corrente:
            contas.append(nova_conta_corrente)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
