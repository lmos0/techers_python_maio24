cardapio = {
    'plain': 'mussarela e molho',
    'calabresa': 'mussarela, calabresa, cebola e molho',
    'frango com catupiry': 'frango, catupiry, mussarela e molho',
    'marguerita': 'tomate, mussarela e molho',
    'portuguesa': 'calabreza, azeitona, cebola, pimentão, ovo, mussarela e molho',
    'francesa': 'presunto, catupiry, ervilha, mussarela e molho'
}

preco = {'plain': 30, 'calabresa': 35, 'frango com catupiry': 37, 'marguerita': 33, 'portuguesa': 40, 'francesa': 42}
item_extra = {'alho': 5, 'abacaxi': 10, 'provolone': 10, 'azeitona': 5, 'borda recheada': 20, 'cebola': 2}

while True:
    pedido = input(f'Peça aqui a sua pizza. Nossos sabores são: {list(cardapio.keys())}\n').lower()
    if pedido in cardapio:
        break
    else:
        continue

while True:
    confirmacao = input(f'O seu pedido foi {pedido}. Para confirmar, digite 1. Se desejar trocar, digite 0: ')
    if confirmacao == '0':
        pedido = input(f'Peça aqui a sua pizza. Nossos sabores são: {list(cardapio.keys())}\n').lower()
    elif confirmacao == '1':
        break
    else:
        print('Opção inválida. Digite 1 para confirmar ou 0 para recomeçar.')

valor_pizza = preco.get(pedido, 0)

while True:
    adicionado = input(f'Você gostaria de adicionar algum desses itens {list(item_extra.keys())}? Digite o nome do item ou 0 para não adicionar nada: ').lower()
    if adicionado == '0':
        break
    elif adicionado in item_extra:
        valor_pizza += item_extra.get(adicionado, 0)
        confirm = input(f'Você adicionou o item "{adicionado}". A informação está correta? Digite 1 para confirmar ou 0 para não adicionar mais nada: ')
        if confirm == '0':
            continue
        elif confirm == '1':
            break
        else:
            print('Opção inválida. Digite 1 para confirmar a adição dos itens ou 0 para não adicionar mais nada.')
    else:
        print(f'O item "{adicionado}" não pode ser adicionado no momento. Tente novamente ou digite 0 para não adicionar nada.')

print(f'O valor total é de R$ {valor_pizza:.2f}')