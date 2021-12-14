from flask import Flask, render_template

from controllers.places_controller import places_blueprint
from controllers.purchases_controller import purchases_blueprint
from controllers.tags_controller import tags_blueprint

app = Flask(__name__)

app.register_blueprint(places_blueprint)
app.register_blueprint(purchases_blueprint)
app.register_blueprint(tags_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)