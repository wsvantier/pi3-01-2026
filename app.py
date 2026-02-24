from flask import Flask
from models import db

app = Flask(__name__)

# Configurações

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Iniciando extensões

db.init_app(app)

@app.route('/')
def home():
    return 'Crianção do app flask'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')