from functions.deposit import deposit
from functions.statement import statement
from functions.withdraw import withdraw
import os

def menu(budget, history):
    withdraw_counter = 0
    message = """-------- Bank V1 ----------

    [D] Para depósito
    [S] Para saque
    [E] Para Extrato
    [Q] Para Sair

"""
    while(True):
        operation = input(message +  "Ação: ")

        if operation.lower() == "q":
            break
        elif operation.lower() == "d":
            value = input("Digite o valor: ")
            budget, history = deposit(float(value),budget, history)
        elif operation.lower() == "e":
            statement(budget, history)
        elif operation.lower() == "s":
            value = input("Digite o valor: ")
            budget, history, withdraw_counter = withdraw(float(value),budget, history, withdraw_counter)
        else:
            print("(ERROR) - Por favor, digite um comando válido!")
