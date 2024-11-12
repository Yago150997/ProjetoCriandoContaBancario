from datetime import datetime
import datetime as dtq


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
LIMITE_SAQUES = 10

while True:

    print(menu)

    opcao = input()

    if opcao == "d":

        valor = float(input("Digite o valor que deseja depositar à conta: "))
        if valor > 0:
            saldo += valor
            extrato += f"valor depositado: R$ {valor:.2f}\n"
        else:
            print("Valor negativo. Por favor, realize nova operação e deposite ao digitar valores positivos.")
    
    elif opcao == "s":

        print("Valor maximo de saque unitário: R$ 500,00")
        saque = int(input("Por favor, digite o valor que deseje sacar: "))
        if saldo >= saque:
            if numero_saques != LIMITE_SAQUES:
                if saque <= 500:
                    saldo -= saque
                    numero_saques += 1
                else:
                    print("Valor excede quantidade na conta. por favor, realize outra operação.")
            else:
                print("Não é possivel sacar mais de R$ 500,00 por vez, por favor, realize outra operação.")

        else:
            print("Numero máximo de saques por dia permitido. Por favor, realize outra operação.")
    elif opcao == "e":
        print("################Extrato#########")
        if(extrato == ""):
            print("Nenhum deposito realizado.")
        else:
            print(extrato)

        print(f"O valor em sua conta é: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Operação invalida. Por favor, selecione outra opção.")