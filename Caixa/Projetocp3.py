def main(): #onde o programa é executado
    carrinho = [] #lista onde joga cada produto como uma tupla 
    total = 0.0 #guarda o valor total da compra

    print("Olá, seja bem-vindo! Fique à vontade para decidir o que comprar.") #exibir mensagem

    while True:
        nome_item = input("Digite o nome do item/produto (ou 'sair' para finalizar): ") #permitir que o usuário adicione itens continuamente
        if nome_item.lower() == 'sair':
            break #ao digitar "sair" o loop é interrompido

        preco_item = float(input("Digite o preço do item: R$"))
        quantidade = int(input("Digite a quantidade do item: "))
        #pede ao usuário o preço(float) e a quantidade do item(int)


        carrinho.append((nome_item, preco_item, quantidade)) #Adiciona uma tupla
        total += preco_item * quantidade #Atualiza o valor total da compra

        print(f"{quantidade}  {nome_item} adicionado ao carrinho.") #Confirma o item adicionado ao carrinho.

        mais_algum = input("Mais algum item? (sim/não): ") #Pergunta se o cliente quer adicionar mais itens.
        if mais_algum.lower() != 'sim':
            break

    while True:
        print("\nItens no carrinho:") #A print exibe os itens no carrinho usando e enumerate para numerar cada item
        for idx, item in enumerate(carrinho):
            print(f"{idx + 1} - {item[2]} x {item[0]}: R${item[1]:.2f} (Total: R${item[1] * item[2]:.2f})")
        print(f"\nTotal da compra: R${total:.2f}") #Exibe o total da compra.


        remover = input("Deseja remover algum item? (sim/não): ") #Pergunta ao cliente se deseja remover um item, se for "sim", pede o número do item a ser removido
        if remover.lower() == 'sim':
            item_remover = int(input("Digite o número do item que deseja remover: ")) - 1 #subtrai o valor do item
            if 0 <= item_remover < len(carrinho):
                total -= carrinho[item_remover][1] * carrinho[item_remover][2]
                del carrinho[item_remover] #Remove o produto do carrinho usando del
                print("Item removido com sucesso.")
            else:
                print("Item inválido.")
        else:
            break


    desconto = 0
    if total > 100:  #
        desconto = total * 0.10
        total -= desconto #Se o total for maior que R$100, aplica um desconto de 10%.
        print(f"Desconto aplicado: R$ {desconto:.2f}")

    forma_pagamento = input("Escolha a forma de pagamento (cartão/dinheiro/pix): ") #Pergunta ao cliente qual será a forma de pagamento

    if forma_pagamento.lower() == 'cartao':
        tipo_cartao = input("É cartão de débito ou crédito? ") #pede o tipo de cartao
        print(f"Forma de pagamento selecionada: {tipo_cartao}.")
        senha_cartao = input("Digite a sua senha: ")
        print("Pagamento realizado com sucesso via cartão.")  #confirma o pagamento

    elif forma_pagamento.lower() == 'dinheiro':
        print(f"Forma de pagamento selecionada: {forma_pagamento}")
        dinheiro = float(input('Quanto de dinheiro você vai dar? R$'))

        if dinheiro >= total:
            troco = dinheiro - total
            print(f'O total foi: R${total:.2f}, e o seu troco é: R${troco:.2f}') #Pergunta ao cliente quanto está pagando em dinheiro e calcula o troco se tiver o valor suficiente
        else:
            print("Valor insuficiente para pagamento.") #avisa quando o valor do pagamento é insuficiente

    elif forma_pagamento.lower() == 'pix':
        print("Forma de pagamento selecionada: PIX.")
        print("Pagamento realizado via PIX.") #confirma o pagamento por pix

    print('Muito obrigada e volte sempre!') #Agradeciento ao cliente


if __name__ == "__main__": #Verifica se o código está sendo executado diretamente
    main()
