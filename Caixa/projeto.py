def main():
    carrinho = []
    total = 0.0

    print("Olá, seja bem-vindo(a) ao Supermercado MatSu! \nFique à vontade para decidir o que comprar!")

    while True:
        nome_item = input("Digite o nome do item/produto (ou 'sair' para finalizar): ")
        if nome_item.lower() == 'sair':
            break

        preco_item = float(input("Digite o preço do produto: R$"))

        carrinho.append((nome_item, preco_item))
        total += preco_item

        print(f"{nome_item} adicionado(a) ao carrinho.")

        mais_algum = input("Mais algum item? (sim/não): ")
        if mais_algum.lower() != 'sim':
            break

    print("\nItens no carrinho:")
    for item in carrinho:
        print(f"- {item[0]}: R${item[1]:.2f}")
    print(f"\nTotal da compra: R${total:.2f}")

   
    forma_pagamento = input("""Escolha a forma de pagamento↓
    Disponível - Cartão, Dinheiro, Pix: """)

    if forma_pagamento.lower() == 'cartao':
        tipo_cartao = input("Cartão de débito ou crédito? ")
        print(f"Forma de pagamento selecionada: {tipo_cartao}.")
        senha_cartao = input("Digite a sua senha: ")
        print("Processando pagamento...")
        time.sleep(3)
        print("Pagamento realizado com sucesso via cartão.")

    elif forma_pagamento.lower() == 'dinheiro':
        print(f"Forma de pagamento selecionada: {forma_pagamento}")
        dinheiro = float(input('Digite o valor em dinheiro: R$'))

        if dinheiro >= total:
            troco = dinheiro - total
            print(f'O total foi: R${total:.2f}, e o seu troco é: R${troco:.2f}')
        else:
            print("Valor insuficiente para efetuar o pagamento. Volte e insira o valor correto...")
            print("Em caso de cancelamento/desistência da compra:")

    elif forma_pagamento.lower() == 'pix':
        print("Forma de pagamento selecionada: PIX.")
        import time
        print("Gerando QR code...")
        time.sleep(3)
        print("QR code gerado!")
        print("Processando pagamento...")
        time.sleep(3)
        print("Pagamento realizado via PIX com sucesso.")


    print('Muito obrigado pela preferência e volte sempre! :)')

if __name__ == "__main__":
    main()