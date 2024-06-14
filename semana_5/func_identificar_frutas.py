#Crie uma função que receba o nome de uma fruta como parâmetro e retorne True se a fruta for cítrica ou False caso não seja  

def identificar_fruta(nome_fruta:str):
    lista_de_frutas_citricas = ['laranja', 'limão', 'tangerina', 'acerola', 'maracuja', 'abacaxi', 'uva', 'kiwi', 'ameixa']
    if nome_fruta in lista_de_frutas_citricas:
        return True
    else:
        return False
    
while True:
    fruta = input('Digite o noma da fruta que deseja consultar. Caso deseje encerrar, digite "sair": ').lower()
    if fruta == "sair":
        break
    resultado = identificar_fruta(fruta)
    print(resultado)
