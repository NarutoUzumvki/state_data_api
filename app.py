from flask import Flask, render_template
from routes.auth import auth_bp
from routes.users import users_bp
from routes.states import states_bp
from routes.ut import ut_bp
from routes.cities import cities_bp
import models
from database_config import engine

app = Flask(__name__)

models.Base.metadata.create_all(bind=engine)

@app.route("/")
def greet():
    return render_template('home.html')

@app.route("/helloworld")
def hello_world():
    return "Hello, World!"

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(states_bp, url_prefix='/states')
app.register_blueprint(ut_bp, url_prefix='/ut')
app.register_blueprint(cities_bp, url_prefix='/cities')


if __name__ == "__main__":
    app.run()