from controller.pedido_controller import criar_pedido
from view.formulario import entrada_usuario

if __name__ == "__main__":
    print("Simular SQL Injection? (s/n): ")
    inj = input().lower() == 's'

    customer_id, employee_id, itens = entrada_usuario(pode_injetar=inj)
    criar_pedido(customer_id, employee_id, itens)

    print("Pedido inserido com sucesso!")
