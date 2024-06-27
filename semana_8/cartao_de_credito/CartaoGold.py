from Cartao_de_credito import CartaodeCredito

class CartaoGold(CartaodeCredito):
    def __init__(self, numero, nome_titular, data_de_validade, codigo_verificador, limite, bandeira):
        super().__init__(numero, nome_titular, data_de_validade, codigo_verificador, limite, bandeira)
        self.cashback_percentual = 0.03
        self.milhas_acumuladas = 0
    
    def __repr__(self):
        return f'Milhas acumuladas: {self.milhas_acumuladas}'
    
    def aplicar_cashback(self, valor_da_compra):
        cashback = valor_da_compra * self.cashback_percentual
        self.limite -= valor_da_compra
        self.limite += cashback
        print(f'Você acumulou R$ {cashback} de cashback na compra de R$ {valor_da_compra}')
    
    def acumular_milhas(self, valor_da_compra):
        milhas = valor_da_compra / 5
        self.limite -= valor_da_compra
        self.milhas_acumuladas += milhas
        print(f'Você acumulou {milhas}, seu saldo atual é de {self.acumular_milhas}')
    
    