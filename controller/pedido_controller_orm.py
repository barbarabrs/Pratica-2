from dao.pedido_dao_orm import inserir_pedido_orm
from datetime import date

class PedidoORM:
    def __init__(self, customer_id, employee_id):
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.order_date = date.today()

class ItemORM:
    def __init__(self, product_id, quantity, unit_price):
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price

def criar_pedido_orm(customer_id, employee_id, itens_dados):
    pedido = PedidoORM(customer_id, employee_id)
    itens = [ItemORM(*i) for i in itens_dados]
    inserir_pedido_orm(pedido, itens)
