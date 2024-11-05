def main():
    carrinho = []
    total = 0.0

    print("Olá, seja bem-vindo! Fique à vontade para decidir o que comprar.")

    while True:
        nome_item = input("Digite o nome do item/produto (ou 'sair' para finalizar): ")
        if nome_item.lower() == 'sair':
            break

        preco_item = float(input("Digite o preço do item: R$"))
        quantidade = int(input("Digite a quantidade do item: "))


        carrinho.append((nome_item, preco_item, quantidade))
        total += preco_item * quantidade

        print(f"{quantidade}  {nome_item} adicionado ao carrinho.")

        mais_algum = input("Mais algum item? (sim/não): ")
        if mais_algum.lower() != 'sim':
            break

    while True:
        print("\nItens no carrinho:")
        for idx, item in enumerate(carrinho):
            print(f"{idx + 1} - {item[2]} x {item[0]}: R${item[1]:.2f} (Total: R${item[1] * item[2]:.2f})")
        print(f"\nTotal da compra: R${total:.2f}")


        remover = input("Deseja remover algum item? (sim/não): ")
        if remover.lower() == 'sim':
            item_remover = int(input("Digite o número do item que deseja remover: ")) - 1
            if 0 <= item_remover < len(carrinho):
                total -= carrinho[item_remover][1] * carrinho[item_remover][2]
                del carrinho[item_remover]
                print("Item removido com sucesso.")
            else:
                print("Item inválido.")
        else:
            break


    desconto = 0
    if total > 100:  #
        desconto = total * 0.10
        total -= desconto
        print(f"Desconto aplicado: R$ {desconto:.2f}")

    forma_pagamento = input("Escolha a forma de pagamento (cartão/dinheiro/pix): ")

    if forma_pagamento.lower() == 'cartao':
        tipo_cartao = input("É cartão de débito ou crédito? ")
        print(f"Forma de pagamento selecionada: {tipo_cartao}.")
        senha_cartao = input("Digite a sua senha: ")
        print("Pagamento realizado com sucesso via cartão.")

    elif forma_pagamento.lower() == 'dinheiro':
        print(f"Forma de pagamento selecionada: {forma_pagamento}")
        dinheiro = float(input('Quanto de dinheiro você vai dar? R$'))

        if dinheiro >= total:
            troco = dinheiro - total
            print(f'O total foi: R${total:.2f}, e o seu troco é: R${troco:.2f}')
        else:
            print("Valor insuficiente para pagamento.")

    elif forma_pagamento.lower() == 'pix':
        print("Forma de pagamento selecionada: PIX.")
        print("Pagamento realizado via PIX.")

    print('Muito obrigada e volte sempre!')


if __name__ == "__main__":
    main()
