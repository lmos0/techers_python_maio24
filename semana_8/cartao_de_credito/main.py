from Cartao_de_credito import CartaodeCredito
from CartaoSilver import CartaoSilver
from CartaoGold import CartaoGold

#Encapsulamento =técnica para esconder detalhes internos, de implementação, de um objeto e expor apenas o necessário.

cartao1 = CartaodeCredito('554433', "luis", "25/06/2030", "874", 3500.00, "Visa" ) #Instancia e cria objeto do tipo cartão
cartao2 = CartaoSilver('85965', 'Lucas', '28/02/2029', '410', 8000.00, "American Express" )
cartao3 = CartaoGold('750284', 'Mariluce', '15/09/2028', '047', 12000.00, 'American Express')
cartao4 = CartaoGold('98322', 'Marcela', '27/06/2025', '747', 12000.00, 'Mastercard')

#cartao1.consultar_limite() #executa o método inerente à classe CartaodeCredito 

# cartao2.consultar_limite()
# cartao2.realizar_compra(500)
# cartao2.consultar_limite()


# cartao2.aplicar_cashback(1000)
# cartao2.consultar_limite()
cartao3.consultar_limite()
cartao3.realizar_compra(300)
cartao3.aplicar_cashback(5000)
cartao3.consultar_limite()
cartao3.pagar_fatura(200)
cartao3.consultar_limite()

cartao3.acumular_milhas(500)

print('#####################################')

cartao3.consultar_limite()
cartao4.realizar_compra(599)
cartao4.aplicar_cashback(4000)
cartao4.acumular_milhas(6000)
cartao4.consultar_limite()
