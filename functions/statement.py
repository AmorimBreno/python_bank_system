import os


def statement(budget, history):
    if history:
        clear = lambda: os.system('cls')
        clear()
        print(f"\n----Extrato---- \n{history}\n-----Saldo----- \nR$ {budget:.2f}")
    else:
        clear = lambda: os.system('cls')
        clear()
        print("Não foram realizadas movimentações.")