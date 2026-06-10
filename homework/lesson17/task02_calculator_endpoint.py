from flask import Flask

app = Flask(__name__)

@app.route("/calc/<func>/<num1>/<num2>")
def calc(func: str, num1: str, num2: str) -> str:
    """Wykonuje wybraną operację matematyczną na dwóch liczbach."""
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return "Podaj poprawne liczby."
    
    func = func.lower()
    
    match func:
        case "add":
            result = num1 + num2
        case "sub":
            result = num1 - num2
        case "mul":
            result = num1 * num2
        case "div":
            if num2 == 0:
                return "Nie można dzielić przez zero!"
            result = num1 / num2
        case _:
            return (
                "Dostępne działania: "
                "add, sub, mul, div"
            )
        
    return f"Wynik to: {result}"

        
if __name__ == "__main__":
    app.run(debug=True)
    
# WERSJA PODSTAWOWA
# from flask import Flask

# app = Flask(__name__)

# @app.route("/add/<int:num1>/<int:num2>")
# def add(num1: int, num2: int) -> str:
#     return f"Wynik to: {num1 + num2}"


# if __name__ == "__main__":
#     app.run(debug=True)