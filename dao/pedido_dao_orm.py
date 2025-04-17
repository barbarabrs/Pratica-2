from db.conexao_orm import Session
from model.models_orm import Orders, OrderDetails
from datetime import date

def inserir_pedido_orm(pedido, itens):
    with Session() as session:
        ultimo = session.query(Orders).order_by(Orders.orderid.desc()).first()
        novoid = 1 if not ultimo else ultimo.orderid + 1

        novopedido = Orders(
            orderid=novoid,
            customerid=pedido.customer_id,
            employeeid=pedido.employee_id,
            orderdate=pedido.order_date or date.today()
        )
        session.add(novopedido)

        for item in itens:
            novoitem = OrderDetails(
                orderid=novoid,
                productid=item.product_id,
                quantity=item.quantity,
                unitprice=item.unit_price
            )
            session.add(novoitem)

        session.commit()
        print(f"✅ Pedido {novoid} inserido com sucesso.")
