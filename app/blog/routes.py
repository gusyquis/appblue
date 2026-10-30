from flask import Blueprint, render_template, abort

blog_bp = Blueprint('blog', __name__, url_prefix='/blog', template_folder='templates')

# Entradas de ejemplo (id -> titulo)
ENTRADAS = {
    1: "Introduccion a Flask",
    2: "Blueprints y modulos",
    3: "Plantillas con Jinja2",
}


# /blog/entrada/1
@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    titulo = ENTRADAS.get(id)
    if titulo is None:
        abort(404)
    return render_template('entrada.html', id=id, titulo=titulo)