#O que é  um cartão de crédito

##### Atributos => Características de um Cartão de Cartão. Serão guardados dentro de variáveis atreladas aos objetos
#numero de identificao
#nome de titular
# data de validade
#codigo verificador
#limite
#bandeira


#### Métodos => Ações pertecentes ao objeto criado (funções)

#comprar
#pagar fatura
#exibir informações
#consultar limite disponível

class CartaodeCredito:
    def __init__ (self, numero, nome_titular, data_de_validade, codigo_verificador, limite, bandeira):
        self.numero = numero
        self.nome_titular = nome_titular
        self.data_de_validade = data_de_validade
        self.codigo_verificador = codigo_verificador
        self.limite = limite
        self.bandeira = bandeira
    
    def realizar_compra(self, valor_da_compra):
        if valor_da_compra <= self.limite:
            self.limite -= valor_da_compra
            print(f'Compra de R$ {valor_da_compra} realizada com sucesso.') 
        else:
            print('Não há limite disponível no momento para concluir esta transação')
    
    def pagar_fatura(self, pagamento_fatura):
        self.limite = self.limite + pagamento_fatura
        print(f'Pagamento de R$ {pagamento_fatura} realizado com sucesso')
        print(f'Seu limite disponível agora é de {self.limite}')
    
    def exibir_informacoes(self):
        print(f'Cartão de Crédito {self.numero}. Titular: {self.nome_titular}' )
        print(f'O Cartão de validade em {self.data_de_validade} e é de bandeira {self.bandeira}')
        
    def consultar_limite(self):
        print(f'O limite atual do cartão é {self.limite}')

