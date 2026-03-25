from flask import Blueprint, render_template

routes_bp = Blueprint('routes_bp', __name__)

@routes_bp.route('/')
def listar_estoque():
    return render_template('estoque/listar.html')

@routes_bp.route('/genero')
def listar_genero():
    return render_template('generos/listar.html')

@routes_bp.route('/consumo')
def listar_consumo():
    return render_template('consumo/listar.html')


