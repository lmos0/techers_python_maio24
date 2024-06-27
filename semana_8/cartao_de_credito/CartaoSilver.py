from Cartao_de_credito import CartaodeCredito

class CartaoSilver(CartaodeCredito):
    def __init__(self, numero, nome_titular, data_de_validade, codigo_verificador, limite, bandeira):
        super().__init__(numero, nome_titular, data_de_validade, codigo_verificador, limite, bandeira)
        self.cashback_percentual = 0.01 #Atributo adicional do cartão do tipo Silver
    
    def aplicar_cashback(self, valor_da_compra):
        cashback = valor_da_compra * self.cashback_percentual
        self.limite -= valor_da_compra
        self.limite += cashback
        print(f'O Cashback de {cashback} foi adicionado ao seu saldo')