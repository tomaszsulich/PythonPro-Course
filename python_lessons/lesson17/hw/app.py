from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/me")
def me():
    return "Tomasz Sulich"

@app.route("/movies")
def movies():
    movies = ["movie1", "movie2", "movie3"]
    return render_template("movie.html",
                           movies = movies,
                           title = "Moje ulubione filmy")

@app.route("/gallery")  
def gallery():
    imgs = [{"url": "https://tse4.mm.bing.net/th/id/OIP.KT0rjWfTkAi67Uv_t_pQNAHaF_?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
             "cap": "Graphic Design vector illustration 10920477 Vector Art at Vecteezy"},
            {"url": "https://public-images.interaction-design.org/literature/articles/materials/ixdf-design-skills-required-by-graphic-artists-and-graphic-designers.png",
             "cap": "Graphic Artist vs. Graphic Designer: What's the difference? | IxDF"}]
    return render_template("gallery.html",
                           imgs = imgs)

@app.route("/calc/<func>/<int:num1><int:num2>")
def calc(func, num1, num2):
    match func:
        case "add":
            return str(num1 + num2)
        case "mul":
            return str(num1 * num2)

        
if __name__ == "__main__":
    app.run(debug=True)