import tkinter as tk
from tkinter import messagebox
from controller.pedido_controller import criar_pedido
from relatorios.relatorio_pedidos import detalhar_pedido
from relatorios.relatorio_funcionarios import ranking_funcionarios
import io
import sys

itens_processados = []

def exibir_saida(func, *args):
    buffer = io.StringIO()
    sys.stdout = buffer
    try:
        func(*args)
    except Exception:
        buffer.write("❌ Erro: Verifique se as datas estão no formato yyyy-mm-dd e não estão vazias.")
    sys.stdout = sys.__stdout__

    texto_resultado.config(state='normal')
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, buffer.getvalue())
    texto_resultado.config(state='disabled')

def adicionar_item():
    try:
        pid = int(entry_produto_id.get())
        qtd = int(entry_quantidade.get())
        preco = float(entry_preco.get())

        itens_processados.append((pid, qtd, preco))
        lista_itens.insert(tk.END, f"Produto ID: {pid}, Qtd: {qtd}, Preço: {preco}")

        entry_produto_id.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Erro", "Preencha os campos do item corretamente.")

def excluir_item():
    try:
        selecionado = lista_itens.curselection()
        if not selecionado:
            raise ValueError("Nenhum item selecionado.")
        indice = selecionado[0]
        lista_itens.delete(indice)
        del itens_processados[indice]
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def enviar_pedido():
    try:
        customer_id = entry_cliente.get()
        employee_id = int(entry_funcionario.get())
        pode_injetar = var_inject.get()

        if not pode_injetar:
            customer_id = customer_id.strip().replace("'", "")

        if not itens_processados:
            raise ValueError("Adicione pelo menos um item ao pedido.")

        criar_pedido(customer_id, employee_id, itens_processados)

        texto_resultado.config(state='normal')
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, "✅ Pedido inserido com sucesso!\n")
        texto_resultado.config(state='disabled')

        itens_processados.clear()
        lista_itens.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Erro","Erro ao salvar o pedido, verifique as informações antes de prosseguir")
def gerar_detalhe_pedido():
    try:
        pedido_id = int(entry_pedido_id.get())
        exibir_saida(detalhar_pedido, pedido_id)
    except Exception:
        messagebox.showerror("Erro!", "Digite um ID de pedido válido.")

def gerar_ranking():
    try:
        inicio = entry_data_inicio.get()
        fim = entry_data_fim.get()
        exibir_saida(ranking_funcionarios, inicio, fim)
    except Exception:
        messagebox.showerror("Erro!", "Verifique se as datas foram preenchidas corretamente.")

app = tk.Tk()
app.title("Sistema de Pedidos")
app.geometry("700x900")

# Campos do pedido
tk.Label(app, text="ID do Cliente").grid(row=0, column=0, sticky='e', padx=10, pady=5)
entry_cliente = tk.Entry(app)
entry_cliente.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="ID do Funcionário").grid(row=1, column=0, sticky='e', padx=10, pady=5)
entry_funcionario = tk.Entry(app)
entry_funcionario.grid(row=1, column=1, padx=10, pady=5)

# Campos dos itens
tk.Label(app, text="ID do Produto").grid(row=2, column=0, sticky='e', padx=10, pady=5)
entry_produto_id = tk.Entry(app)
entry_produto_id.grid(row=2, column=1, padx=10, pady=5)

tk.Label(app, text="Quantidade").grid(row=3, column=0, sticky='e', padx=10, pady=5)
entry_quantidade = tk.Entry(app)
entry_quantidade.grid(row=3, column=1, padx=10, pady=5)

tk.Label(app, text="Preço Unitário").grid(row=4, column=0, sticky='e', padx=10, pady=5)
entry_preco = tk.Entry(app)
entry_preco.grid(row=4, column=1, padx=10, pady=5)

tk.Button(app, text="Adicionar Item", command=adicionar_item).grid(row=5, column=0, columnspan=2, pady=5)

# Lista de itens adicionados
tk.Label(app, text="Itens do Pedido:").grid(row=6, column=0, columnspan=2, pady=(10, 0))
lista_itens = tk.Listbox(app, width=60, height=5)
lista_itens.grid(row=7, column=0, columnspan=2, padx=10)

tk.Button(app, text="❌ Excluir Item Selecionado", command=excluir_item).grid(row=8, column=0, columnspan=2, pady=5)

# Checkbox para SQL Injection
var_inject = tk.BooleanVar()
tk.Checkbutton(app, text="Simular SQL Injection", variable=var_inject).grid(row=9, column=0, columnspan=2, pady=5)

# Botão de envio
tk.Button(app, text="Enviar Pedido", command=enviar_pedido).grid(row=10, column=0, columnspan=2, pady=10)

# Relatório - Detalhar pedido
tk.Label(app, text="ID do Pedido").grid(row=11, column=0, sticky='e', padx=10, pady=5)
entry_pedido_id = tk.Entry(app)
entry_pedido_id.grid(row=11, column=1, padx=10, pady=5)

tk.Button(app, text="Detalhar Pedido", command=gerar_detalhe_pedido).grid(row=12, column=0, columnspan=2, pady=5)

# Relatório - Ranking
tk.Label(app, text="Data Início (YYYY-MM-DD)").grid(row=13, column=0, sticky='e', padx=10, pady=5)
entry_data_inicio = tk.Entry(app)
entry_data_inicio.grid(row=13, column=1, padx=10, pady=5)

tk.Label(app, text="Data Fim (YYYY-MM-DD)").grid(row=14, column=0, sticky='e', padx=10, pady=5)
entry_data_fim = tk.Entry(app)
entry_data_fim.grid(row=14, column=1, padx=10, pady=5)

tk.Button(app, text="Gerar Ranking", command=gerar_ranking).grid(row=15, column=0, columnspan=2, pady=10)

# Área de exibição de resultados
tk.Label(app, text="📋 Saída dos Relatórios:").grid(row=16, column=0, columnspan=2)
texto_resultado = tk.Text(app, height=15, width=80, state='disabled', bg="#f4f4f4")
texto_resultado.grid(row=17, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()