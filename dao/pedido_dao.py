from db.conexao import conectar

def inserir_pedido(pedido):
    with conectar() as conn:
        with conn.cursor() as cur:
            
            cur.execute("SELECT MAX(orderid) AS ultimo_id FROM NORTHWIND.orders")
            ultimo_id = cur.fetchone()["ultimo_id"] or 0
            novo_order_id = ultimo_id + 1
            
            cur.execute("""
                INSERT INTO northwind.orders (orderid, customerid, employeeid, orderdate)
                VALUES (%s, %s, %s, %s)
                RETURNING orderid
            """, (novo_order_id,pedido.customer_id, pedido.employee_id, pedido.order_date))

            for item in pedido.itens:
                cur.execute("""
                    INSERT INTO northwind.order_details (orderid, productid, quantity, unitprice)
                    VALUES (%s, %s, %s, %s)
                """, (novo_order_id, item.product_id, item.quantity, item.unit_price))

        conn.commit()
