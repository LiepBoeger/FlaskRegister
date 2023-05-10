from flask import Flask
from models.db import db
from models import usuario_models
from routes import cadastro_route, login_route, home_route, logout_route, cadastro_jogador_route
from flask_login import LoginManager

# configuração da aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuario.sqlite3'
app.config['SECRET_KEY'] = 'secretkey'

# registra o Blueprint das rotas de usuário
app.register_blueprint(cadastro_route.cadastro_route_bp)
app.register_blueprint(login_route.login_route_bp)
app.register_blueprint(home_route.home_route_bp)
app.register_blueprint(logout_route.logout_route_bp)
app.register_blueprint(cadastro_jogador_route.cadastro_jogador_route_bp)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return usuario_models.Usuario.query.get(int(user_id))

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
