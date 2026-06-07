from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Witaj na stronie głównej!"

@app.route("/about")
def about():
    return "To jest strona o nas."

@app.route("/contact")
def contact():
    return "Tutaj znajdziesz nasz kontakt."


if __name__ == "__main__":
    app.run(debug=True)