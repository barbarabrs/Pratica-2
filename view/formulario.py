def entrada_usuario(pode_injetar=False):
    if pode_injetar:
        customer_id = input("Digite o ID do cliente (permite SQL injection): ")
    else:
        customer_id = input("Digite o ID do cliente (seguro): ").strip().replace("'", "")

    employee_id = int(input("ID do funcionário: "))
    qtd_itens = int(input("Quantos itens? "))

    itens = []
    for _ in range(qtd_itens):
        pid = int(input("ID do produto: "))
        qnt = int(input("Quantidade: "))
        price = float(input("Preço unitário: "))
        itens.append((pid, qnt, price))

    return customer_id, employee_id, itens
