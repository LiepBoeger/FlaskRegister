from flask import Flask
from models.db import db
from routes.user_routes import user_routes_bp
from routes.login_route import login_route_bp

# configuração da aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuario.sqlite3'
app.config['SECRET_KEY'] = 'secretkey'

# registra o Blueprint das rotas de usuário
app.register_blueprint(user_routes_bp)
app.register_blueprint(login_route_bp)

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
