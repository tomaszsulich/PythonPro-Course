from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Strona główna. Spróbuj wejść na /user/twoje_imie"

@app.route("/user/<username>", methods = ["GET", "POST"])
def show_user_profile(username):
    return f"Witaj, {username}!"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Wyświetlasz post o ID: {post_id}"


if __name__ == "__main__":
    app.run(debug=True)