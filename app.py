"""
CadastroPro - CRUD de Cadastro de Pessoas
Flask + SQLite com Dashboard, ViaCEP e Export PDF
"""

from flask import Flask, render_template, request, redirect, url_for, flash, Response
import sqlite3
import os
import re
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'chave-secreta-crud-pessoas-2026'

DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pessoas.db')


def get_db():
    conn = sqlite3.connect(DATABASE, timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL,
            cidade TEXT DEFAULT '',
            estado TEXT DEFAULT '',
            cep TEXT DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[9]):
        return False
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        return False
    return True


def formatar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) == 11:
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return cpf


def formatar_telefone(tel):
    tel = re.sub(r'[^0-9]', '', tel)
    if len(tel) == 11:
        return f'({tel[:2]}) {tel[2:7]}-{tel[7:]}'
    elif len(tel) == 10:
        return f'({tel[:2]}) {tel[2:6]}-{tel[6:]}'
    return tel


# ========== ROTAS ==========

@app.route('/')
def index():
    conn = get_db()
    pessoas = conn.execute('SELECT * FROM pessoas ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', pessoas=pessoas)


@app.route('/dashboard')
def dashboard():
    conn = get_db()
    total = conn.execute('SELECT COUNT(*) as c FROM pessoas').fetchone()['c']
    por_estado = conn.execute(
        'SELECT estado, COUNT(*) as c FROM pessoas WHERE estado != "" GROUP BY estado ORDER BY c DESC'
    ).fetchall()
    recentes = conn.execute('SELECT * FROM pessoas ORDER BY created_at DESC LIMIT 5').fetchall()
    conn.close()
    estados_labels = json.dumps([r['estado'] for r in por_estado])
    estados_data = json.dumps([r['c'] for r in por_estado])
    return render_template('dashboard.html', total=total, por_estado=por_estado,
                           recentes=recentes, estados_labels=estados_labels, estados_data=estados_data)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        cpf = request.form.get('cpf', '').strip()
        telefone = request.form.get('telefone', '').strip()
        endereco = request.form.get('endereco', '').strip()
        cidade = request.form.get('cidade', '').strip()
        estado = request.form.get('estado', '').strip()
        cep = request.form.get('cep', '').strip()

        erros = []
        if not nome: erros.append('Nome e obrigatorio.')
        if not cpf: erros.append('CPF e obrigatorio.')
        elif not validar_cpf(cpf): erros.append('CPF invalido.')
        if not telefone: erros.append('Telefone e obrigatorio.')
        if not endereco: erros.append('Endereco e obrigatorio.')

        if erros:
            for e in erros: flash(e, 'error')
            return render_template('form.html', pessoa={
                'nome': nome, 'cpf': cpf, 'telefone': telefone,
                'endereco': endereco, 'cidade': cidade, 'estado': estado, 'cep': cep
            }, acao='Cadastrar')

        try:
            conn = get_db()
            conn.execute(
                'INSERT INTO pessoas (nome, cpf, telefone, endereco, cidade, estado, cep) VALUES (?,?,?,?,?,?,?)',
                (nome, formatar_cpf(cpf), formatar_telefone(telefone), endereco, cidade, estado, cep)
            )
            conn.commit()
            conn.close()
            flash('Pessoa cadastrada com sucesso!', 'success')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            conn.close()
            flash('CPF ja cadastrado no sistema.', 'error')
            return render_template('form.html', pessoa={
                'nome': nome, 'cpf': cpf, 'telefone': telefone,
                'endereco': endereco, 'cidade': cidade, 'estado': estado, 'cep': cep
            }, acao='Cadastrar')

    return render_template('form.html', pessoa={}, acao='Cadastrar')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_db()
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        cpf = request.form.get('cpf', '').strip()
        telefone = request.form.get('telefone', '').strip()
        endereco = request.form.get('endereco', '').strip()
        cidade = request.form.get('cidade', '').strip()
        estado = request.form.get('estado', '').strip()
        cep = request.form.get('cep', '').strip()

        erros = []
        if not nome: erros.append('Nome e obrigatorio.')
        if not cpf: erros.append('CPF e obrigatorio.')
        elif not validar_cpf(cpf): erros.append('CPF invalido.')
        if not telefone: erros.append('Telefone e obrigatorio.')
        if not endereco: erros.append('Endereco e obrigatorio.')

        if erros:
            for e in erros: flash(e, 'error')
            conn.close()
            return render_template('form.html', pessoa={
                'id': id, 'nome': nome, 'cpf': cpf, 'telefone': telefone,
                'endereco': endereco, 'cidade': cidade, 'estado': estado, 'cep': cep
            }, acao='Editar')

        try:
            conn.execute(
                'UPDATE pessoas SET nome=?, cpf=?, telefone=?, endereco=?, cidade=?, estado=?, cep=? WHERE id=?',
                (nome, formatar_cpf(cpf), formatar_telefone(telefone), endereco, cidade, estado, cep, id)
            )
            conn.commit()
            conn.close()
            flash('Dados atualizados com sucesso!', 'success')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            conn.close()
            flash('CPF ja cadastrado para outra pessoa.', 'error')
            return render_template('form.html', pessoa={
                'id': id, 'nome': nome, 'cpf': cpf, 'telefone': telefone,
                'endereco': endereco, 'cidade': cidade, 'estado': estado, 'cep': cep
            }, acao='Editar')

    pessoa = conn.execute('SELECT * FROM pessoas WHERE id = ?', (id,)).fetchone()
    conn.close()
    if not pessoa:
        flash('Pessoa nao encontrada.', 'error')
        return redirect(url_for('index'))
    return render_template('form.html', pessoa=pessoa, acao='Editar')


@app.route('/excluir/<int:id>', methods=['GET', 'POST'])
def excluir(id):
    conn = get_db()
    conn.execute('DELETE FROM pessoas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Pessoa excluida com sucesso!', 'success')
    return redirect(url_for('index'))


@app.route('/visualizar/<int:id>')
def visualizar(id):
    conn = get_db()
    pessoa = conn.execute('SELECT * FROM pessoas WHERE id = ?', (id,)).fetchone()
    conn.close()
    if not pessoa:
        flash('Pessoa nao encontrada.', 'error')
        return redirect(url_for('index'))
    return render_template('visualizar.html', pessoa=pessoa)


@app.route('/buscar')
def buscar():
    termo = request.args.get('q', '').strip()
    conn = get_db()
    if termo:
        pessoas = conn.execute(
            'SELECT * FROM pessoas WHERE nome LIKE ? OR cpf LIKE ? ORDER BY nome',
            (f'%{termo}%', f'%{termo}%')
        ).fetchall()
    else:
        pessoas = conn.execute('SELECT * FROM pessoas ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', pessoas=pessoas, termo_busca=termo)


@app.route('/exportar/csv')
def exportar_csv():
    conn = get_db()
    pessoas = conn.execute('SELECT * FROM pessoas ORDER BY nome').fetchall()
    conn.close()
    lines = ['ID;Nome;CPF;Telefone;Endereco;Cidade;Estado;CEP']
    for p in pessoas:
        lines.append(f'{p["id"]};{p["nome"]};{p["cpf"]};{p["telefone"]};{p["endereco"]};{p["cidade"]};{p["estado"]};{p["cep"]}')
    csv_content = '\n'.join(lines)
    return Response(
        csv_content,
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment;filename=cadastros_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'}
    )


if __name__ == '__main__':
    init_db()
    print('\n' + '=' * 50)
    print('  CRUD de Cadastro de Pessoas')
    print('  Acesse: http://localhost:5000')
    print('=' * 50 + '\n')
    app.run(debug=True, port=5000)
