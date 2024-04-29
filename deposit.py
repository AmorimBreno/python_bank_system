def deposit(value, budget, history):
    if (value > 500) or (value <= 0):
        print("(ERROR) - Valor inválido!")
        exit
    else:
        budget += value
        history += f"Depósito: R$ {value:.2f}\n"
        print("(SYSTEM) - Depósito realizado com SUCESSO!")
    
    return budget, history