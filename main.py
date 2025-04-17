from controller.pedido_controller import criar_pedido
from controller.pedido_controller_orm import criar_pedido_orm
from view.formulario import entrada_usuario
from relatorios.relatorio_pedidos import detalhar_pedido
from relatorios.relatorio_funcionarios import ranking_funcionarios
from interface import App

if __name__ == "__main__":
    print("Simular SQL Injection? (s/n): ")
    inj = input().lower() == 's'

    customer_id, employee_id, itens = entrada_usuario(pode_injetar=inj)

    if inj:
        print("\n🔐 Usando psycopg (com possível SQL Injection)...")
        criar_pedido(customer_id, employee_id, itens)
    else:
        print("\n🛡️ Usando SQLAlchemy (ORM)...")
        criar_pedido_orm(customer_id, employee_id, itens)

    print("\n✅ Pedido inserido com sucesso!\n")

    # Relatório 1 - Detalhar pedido
    pedido_id = int(input("Digite o número do pedido para detalhar: "))
    detalhar_pedido(pedido_id)

    # Relatório 2 - Ranking funcionários
    inicio = input("\nData início (YYYY-MM-DD): ")
    fim = input("Data fim (YYYY-MM-DD): ")
    ranking_funcionarios(inicio, fim)
    
