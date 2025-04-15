from db.conexao import conectar

def ranking_funcionarios(inicio, fim):
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    e.firstname || ' ' || e.lastname AS funcionario,
                    COUNT(DISTINCT o.orderid) AS total_pedidos,
                    SUM(od.quantity * od.unitprice) AS total_vendido
                FROM northwind.employees e
                JOIN northwind.orders o ON e.employeeid = o.employeeid
                JOIN northwind.order_details od ON o.orderid = od.orderid
                WHERE o.orderdate BETWEEN %s AND %s
                GROUP BY funcionario
                ORDER BY total_vendido DESC
            """, (inicio, fim))

            ranking = cur.fetchall()

            if not ranking:
                print("Nenhum dado encontrado nesse intervalo.")
                return

            print(f"\n📈 Ranking de {inicio} até {fim}:\n")
            for i, f in enumerate(ranking, 1):
                print(f"{i}. {f['funcionario']}")
                print(f"   Pedidos: {f['total_pedidos']} | Total vendido: ${f['total_vendido']:.2f}")
