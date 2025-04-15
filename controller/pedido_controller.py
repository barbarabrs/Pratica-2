from model.models import Pedido, ItemPedido
from dao.pedido_dao import inserir_pedido
from datetime import date

def criar_pedido(customer_id, employee_id, itens_dados):
    pedido = Pedido(customer_id, employee_id, date.today())
    for item in itens_dados:
        pedido.itens.append(ItemPedido(*item))
    inserir_pedido(pedido)
