from flask import Flask

app = Flask(__name__)

@app.route("/me")
def me() -> str:
    """Zwraca podstawowe informacje o autorze strony."""
    return "Tomasz Sulich"


if __name__ == "__main__":
    app.run(debug=True)