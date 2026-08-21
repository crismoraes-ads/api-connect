from flask import Flask
from routes.usuarios import usuarios_bp

app = Flask(__name__)

app.register_blueprint(usuarios_bp)


@app.route("/")
def inicio():
    return {
        "mensagem": "API Connect em funcionamento."
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)