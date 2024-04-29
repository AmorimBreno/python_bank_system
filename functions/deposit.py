import os

def deposit(value, budget, history):
    if (value <= 0):
        print("(ERROR) - Valor inválido!")
        exit
    else:
        budget += value
        clear = lambda: os.system('cls')
        clear()
        history += f"Depósito: R$ {value:.2f}\n"
        print("(SYSTEM) - Depósito realizado com SUCESSO!\n")
    
    return budget, history