import os


def withdraw(value, budget, history, withdraw_count):
    if (value > 500) or (value <= 0):
        clear = lambda: os.system('cls')
        clear()
        print("(ERROR) - Valor inválido!\n")
        exit
    elif value > budget:
        clear = lambda: os.system('cls')
        clear()
        print("(ERROR) - Saldo insuficiente!\n")
        exit
    elif withdraw_count >= 3:
        clear = lambda: os.system('cls')
        clear()
        print("(ERROR) - Número máximo de saques por dia atingido!\n")
        exit
    else:
        budget -= value
        clear = lambda: os.system('cls')
        clear()
        history += f"Saque: R$ {value:.2f}\n"
        withdraw_count += 1
        print("(SYSTEM) - Saque realizado com SUCESSO!\n")
    
    return budget, history, withdraw_count