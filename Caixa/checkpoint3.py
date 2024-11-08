import time

def adicionar_item(carrinho, total):
    nome_item = input("Digite o nome do produto (ou 'sair' para finalizar): ")
    if nome_item.lower() == 'sair':
        return carrinho, total, False

    preco_item = float(input("Digite o preço do produto: R$"))
    quantidade = int(input("Digite a quantidade do produto: "))

    carrinho.append((nome_item, preco_item, quantidade))
    total += preco_item * quantidade

    print(f"{quantidade} {nome_item} adicionado ao carrinho.")
    return carrinho, total, True


def remover_item(carrinho, total):
    print("\nItens no carrinho:")
    for idx, item in enumerate(carrinho):
        nome_item, preco_item, quantidade_item = item
        print(f"{idx + 1} - {quantidade_item} x {nome_item}: R${preco_item:.2f} (Total: R${preco_item * quantidade_item:.2f})")
    print(f"\nTotal da compra: R${total:.2f}")

    remover = input("Deseja remover algum produto? (sim/não): ")
    if remover.lower() == 'sim':
        item_remover = int(input("Digite o número do item que deseja remover: ")) - 1
        if 0 <= item_remover < len(carrinho):
            nome_item, preco_item, quantidade_item = carrinho[item_remover]
            quantidade_remover = int(input(f"Quantos {nome_item} você deseja remover? (Máximo {quantidade_item}): "))
            if 0 < quantidade_remover <= quantidade_item:
                carrinho[item_remover] = (nome_item, preco_item, quantidade_item - quantidade_remover)
                total -= preco_item * quantidade_remover
                print(f"{quantidade_remover} {nome_item}(s) removido(s) com sucesso.")
                if carrinho[item_remover][2] == 0:
                    del carrinho[item_remover]
                    print(f"Todos os {nome_item}(s) foram removidos do carrinho.")
            else:
                print("Quantidade inválida. Não foi possível remover o produto.")
        else:
            print("Número de produto inválido.")
    return carrinho, total


def aplicar_desconto(total):
    desconto = 0
    if total > 100:
        desconto = total * 0.10
        total -= desconto
        print(f"Desconto aplicado: R$ {desconto:.2f}")
    return total


def escolher_pagamento(total):
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
        print(f"Valor da compra antes do pagamento: R${total:.2f}")
        print("Forma de pagamento selecionada: PIX.")
        time.sleep(2)
        print("Gerando o QR Code...")
        time.sleep(3)
        print("QR Code gerado!")
        print("Pagamento realizado via PIX com sucesso!")

    return forma_pagamento


def main():
    print("Olá, seja bem-vindo(a) ao supermercado SUMATT!")
    print("Fique à vontade para decidir o que comprar e o que remover do seu carrinho.")

    carrinho = []
    total = 0.0

    while True:
        carrinho, total, continuar = adicionar_item(carrinho, total)
        if not continuar:
            break

        mais_algum = input("Mais algum produto? (sim/não): ")
        if mais_algum.lower() != 'sim':
            break

    while True:
        carrinho, total = remover_item(carrinho, total)
        continuar_remover = input("Deseja remover mais algum produto? (sim/não): ")
        if continuar_remover.lower() != 'sim':
            break

    total = aplicar_desconto(total)

    forma_pagamento = escolher_pagamento(total)

    print(f"\nTotal da compra: R${total:.2f}")
    print('Muito obrigada e volte sempre!')


if __name__ == "__main__":
    main()
