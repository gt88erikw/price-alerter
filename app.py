__author__ = 'gt88e'
from flask import Flask, render_template
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint
from random import randint


app = Flask(__name__)
app.secret_key = str(randint(10000000000, 99999999999))
app.config.from_object('config')


@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(user_blueprint, url_prefix="/users")

if __name__ == '__main__':
    app.run(debug=True)
