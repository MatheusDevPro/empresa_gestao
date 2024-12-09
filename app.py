from flask import Flask, render_template, request, redirect, url_for
import pyodbc
from database import get_connection

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página financeira
@app.route('/financeiro')
def financeiro():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Financeiro")
    registros = cursor.fetchall()
    conn.close()
    return render_template('financeiro.html', registros=registros)

# Rota para a página RH
@app.route('/rh')
def rh():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Funcionarios")
    funcionarios = cursor.fetchall()
    conn.close()
    return render_template('rh.html', funcionarios=funcionarios)

# Rota para a página de estoque
@app.route('/estoque')
def estoque():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produtos")
    produtos = cursor.fetchall()
    conn.close()
    return render_template('estoque.html', produtos=produtos)

# Rota para cadastrar produto
@app.route('/cadastro_produto', methods=['GET', 'POST'])
def cadastro_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        quantidade = request.form['quantidade']
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Produtos (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
            (nome, descricao, preco, quantidade)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('estoque'))

    return render_template('cadastro_produto.html')

# Rota para pedidos
@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    if request.method == 'POST':
        produto_id = request.form['produto_id']
        quantidade = request.form['quantidade']
        valor = request.form['valor']
        prazo_entrega = request.form['prazo_entrega']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Pedidos (produto_id, quantidade, valor, prazo_entrega)
            VALUES (?, ?, ?, ?)
        """, (produto_id, quantidade, valor, prazo_entrega))
        conn.commit()
        conn.close()

        return redirect(url_for('pedidos'))  # Redireciona para a lista de pedidos ou outra página

    return render_template('pedidos.html')
