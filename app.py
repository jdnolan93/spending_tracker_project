from flask import Flask, render_template

#INSERT import of blueprints from controllers here


app = Flask(__name__)

#INSERT app.register_blueprint here

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()