from db.conexao import conectar

def inserir_pedido(pedido):
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO orders (customer_id, employee_id, order_date)
                VALUES (%s, %s, %s)
                RETURNING order_id
            """, (pedido.customer_id, pedido.employee_id, pedido.order_date))
            order_id = cur.fetchone()["order_id"]

            for item in pedido.itens:
                cur.execute("""
                    INSERT INTO order_details (order_id, product_id, quantity, unit_price)
                    VALUES (%s, %s, %s, %s)
                """, (order_id, item.product_id, item.quantity, item.unit_price))

        conn.commit()
