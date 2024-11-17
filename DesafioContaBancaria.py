from datetime import datetime
import datetime as dtq

saldo = 0
limite = 500
extrato_saldo = ""
numero_saques = 0
LIMITE_SAQUES = 9
Data_Saque = []


def depositar(valor):

            global saldo 
            saldo += valor
            global extrato_saldo
            extrato_saldo += f"valor depositado: R$ {saldo:.2f}\n"


def saque(valor_saque):

    global LIMITE_SAQUES
    global saldo
    global numero_saques
    global Data_Saque


    if numero_saques != LIMITE_SAQUES:

        if saldo >= valor_saque:

            if valor_saque <= limite:

                saldo -= valor_saque
                numero_saques += 1
                extrato_saldo = saldo
                Registro = datetime.now().strftime('%d/%m/%y %H:%M:%S')
                
                Data_Saque.append(f"{Registro} " + f"R$ {valor_saque:.2f}")

                return numero_saques,saldo,extrato_saldo
            else:
                print("Valor excede quantidade na conta. por favor, realize outra operação.")
        else:
            print("Não é possivel sacar mais de R$ 500,00 por vez, por favor, realize outra operação.")
    else:
        print("Numero máximo de saques por dia permitido. Por favor, realize outra operação.")

def Extrato():

    global extrato
    print("################Extrato#########")
    if(extrato_saldo == ""):
        print("Nenhum deposito ou saque realizado.")
    else:

        print(extrato_saldo)
        
        print()

        for d in Data_Saque:
            print(d)
  
    
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:

    print(menu)

    opcao = input()

    if opcao == "d":

        valor = float(input("Digite o valor que deseja depositar à conta: "))

        if valor > 0:
            depositar(valor)
            
        else:
            print("Valor negativo. Por favor, realize nova operação e deposite ao digitar valores positivos.")

    
    elif opcao == "s":
        
       print("Valor maximo de saque unitário: R$ 500,00")
       valor_saque = int(input("Por favor, digite o valor que deseje sacar: "))
       saque(valor_saque)

    elif opcao == "e":

        Extrato()

        print(f"O valor em sua conta é: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Operação invalida. Por favor, selecione outra opção.")