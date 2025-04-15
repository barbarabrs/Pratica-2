class Pedido:
    def __init__(self, customer_id, employee_id, order_date):
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.order_date = order_date
        self.itens = []

class ItemPedido:
    def __init__(self, product_id, quantity, unit_price):
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
