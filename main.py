from controller.pedido_controller import criar_pedido
from view.formulario import entrada_usuario
from relatorios.relatorio_pedidos import detalhar_pedido
from relatorios.relatorio_funcionarios import ranking_funcionarios

if __name__ == "__main__":
    print("Simular SQL Injection? (s/n): ")
    inj = input().lower() == 's'

    customer_id, employee_id, itens = entrada_usuario(pode_injetar=inj)
    criar_pedido(customer_id, employee_id, itens)
    #relatorio 1
    print("Pedido inserido com sucesso!")
    pedido_id = int(input("Digite o número do pedido para detalhar: "))
    detalhar_pedido(pedido_id)
    #relatorio 2
    inicio = input("Data início (YYYY-MM-DD): ")
    fim = input("Data fim (YYYY-MM-DD): ")
    ranking_funcionarios(inicio, fim)
