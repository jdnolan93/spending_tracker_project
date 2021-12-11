from flask import Flask, render_template

from controllers.places_controller import places_blueprint
from controllers.purchases_controller import purchases_blueprint

app = Flask(__name__)

app.register_blueprint(places_blueprint)
app.register_blueprint(purchases_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()