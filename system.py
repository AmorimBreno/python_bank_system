from deposit import deposit

budget = 0
history = ""

budget,history = deposit(300,budget,history)
budget,history = deposit(400,budget,history)

print(f"\n-----Saldo----- \nR$ {budget:.2f}\n----Extrato---- \n{history}")