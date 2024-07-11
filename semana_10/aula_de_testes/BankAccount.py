class BankAccount:
    def __init__(self, initial_balance=0):
     self.balance = initial_balance 


    def deposit(self, amount):
       if amount <= 0:
          raise ValueError('O valor do depósito precisa ser positivo')
       self.balance += amount
       return self.balance
    
    def withdraw(self, amount):
       if amount <= 0:
          raise ValueError('O valor do saque precisa ser positivo')
       if amount > self.balance:
          raise ValueError('Saldo insuficiente')
       self.balance -= amount
       return self.balance
    
    def get_balance(self):
       return self.balance