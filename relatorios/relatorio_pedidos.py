# relatorios/relatorio_pedidos.py
from db.conexao import conectar

def detalhar_pedido(order_id):
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("SET CLIENT_ENCODING TO 'UTF8'")
            # Info geral do pedido
            cur.execute("""
                SELECT 
                    o.orderid,
                    o.orderdate,
                    c.companyname AS cliente,
                    e.firstname || ' ' || e.lastname AS vendedor
                FROM northwind.orders o
                JOIN northwind.customers c ON o.customerid = c.customerid
                JOIN northwind.employees e ON o.employeeid = e.employeeid
                WHERE o.orderid = %s
            """, (order_id,))
            pedido = cur.fetchone()

            if not pedido:
                print(f"Pedido {order_id} não encontrado.")
                return

            print("\n📦 Pedido:")
            print(f"ID: {pedido['orderid']}")
            print(f"Data: {pedido['orderdate']}")
            print(f"Cliente: {pedido['cliente']}")
            print(f"Vendedor: {pedido['vendedor']}\n")

            # Itens do pedido
            cur.execute("""
                SELECT 
                    p.productname,
                    od.quantity,
                    od.unitprice
                FROM northwind.order_details od
                JOIN northwind.products p ON od.productid = p.productid
                WHERE od.orderid = %s
            """, (order_id,))
            itens = cur.fetchall()

            print("🧾 Itens:")
            for item in itens:
                print(f"- {item['productname']}: {item['quantity']} x ${item['unitprice']:.2f}")
