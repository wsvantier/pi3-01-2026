from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from .models import db, Lote, Produto 
from datetime import datetime 


routes_bp = Blueprint('routes_bp', __name__) 

### Estoque ###

# Pagina inicial do Estoque
@routes_bp.route('/') 
def listar_estoque(): 
    return render_template('estoque/listar.html')

# Pagina para inserir novos lotes
@routes_bp.route('/estoque/form') 
def form_estoque():
    produtos = Produto.query.filter_by(ativo=True).all() # Dados para o select do HTML
    return render_template('estoque/form.html', produtos = produtos)

# Rota para inserir itens no banco de dados, (action do form)
@routes_bp.route('/estoque/inserir', methods = ['POST']) 
def inserir_lote(): 
    genero = request.form['genero']
    entrada = datetime.strptime(request.form['entrada'], '%Y-%m-%d')
    validade = datetime.strptime(request.form['validade'], '%Y-%m-%d')
    quantidade = int(request.form['quant']) 
    novo_lote = Lote(
        produto_id = genero,
        data_recebimento = entrada,
        data_validade = validade,
        quantidade_inicial = quantidade)
    
    try: 
        db.session.add(novo_lote)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    
    return redirect(url_for('routes_bp.listar_estoque')) 
    
### Gênero ###
    
# Pagina Inicial do Gênero 
@routes_bp.route('/genero')
def listar_genero(): 
    return render_template('generos/listar.html') 

# Pagina para inserir novos gêneros 
@routes_bp.route('/genero/form') 
def form_genero(): 
    return render_template('generos/form.html') 

# Rota para o action do form, para inserir dados no banco

@routes_bp.route('/genero/inserir', methods = ['POST'])
def inserir_genero():
    genero = request.form['genero']
    medida = request.form['medida']
    minimo = request.form['min']
    
    novo_produto = Produto(nome = genero,
                           unidade_medida = medida,
                           estoque_minimo = minimo)
    
    try:
        db.session.add(novo_produto)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    
    return redirect(url_for('routes_bp.listar_estoque'))
    
# API para listar o gênero    

@routes_bp.route('/api/genero')
def api_genero():
    busca = Produto.query.all()
    dados = [{'id':i.id,
              'nome':i.nome,
              'unidade_medida':i.unidade_medida,
              'estoque_minimo':i.estoque_minimo,
              'ativo':i.ativo
              } for i in busca]
    
    return jsonify(dados)
    
    
    

    
### Consumo ###

# Pagina inicial da parte de consumo
@routes_bp.route('/consumo')
def listar_consumo(): 
    return render_template('consumo/listar.html')

# Cadastro de consumo
@routes_bp.route('/consumo/form') 
def form_consumo():
    return render_template('consumo/form.html')