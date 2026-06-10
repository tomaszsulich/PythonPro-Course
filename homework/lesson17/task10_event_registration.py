from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///event_registrations.db'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Registration(db.Model):
    """
    Reprezentuje zgłoszenie uczestnika na wydarzenie.
    
    Łączy dane identyfikujące osobę z informacjami
    niezbędnymi do ewidencjonowania zgłoszeń
    oraz kontroli ich unikalności.
    """
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    @classmethod
    def create(cls, name: str, email: str) -> tuple[Registration | None, list[str]]:
        """
        Przeprowadza proces rejestracji uczestnika.
        
        Dba o spójność zgromadzonych informacji,
        wychwytuje nieprawidłowe zgłoszenia
        oraz zapobiega wielokrotnemu zapisaniu
        tej samej osoby.
        """
        
        name = name.strip().capitalize()
        email = email.strip().lower()
        
        errors: list[str] = []
        
        if not name:
            errors.append("Imię nie może być puste!")
            
        if not email:
            errors.append("Email nie może być pusty!")
            
        if " " in email:
            errors.append("Email nie może zawierać spacji!")
            
        if email.count("@") != 1:
            errors.append("Email musi zawierać dokładnie jeden znak @!")
        else:
            local_part, domain = email.split("@")
            
            if not local_part:
                errors.append("Email musi zawierać nazwę przed znakiem @!")
                
            if not domain:
                errors.append("Email musi zawierać domenę po znaku @!")
                
            if "." not in domain:
                errors.append("Domena emaila musi zawierać kropkę!")
                
            if domain.startswith(".") or domain.endswith("."):
                errors.append("Domena emaila nie może zaczynać ani kończyć się kropką!")
        
        if errors:
            return None, errors
        
        existing_registration = cls.query.filter_by(
            email = email
        ).first()
        
        if existing_registration:
            return None, ["Ten email jest już zapisany!"]
        
        return cls(
            name = name,
            email = email,
        ), []
        
@app.route("/register", methods=["GET", "POST"])
def register() -> Response | str:
    """
    Obsługuje formularz rejestracyjny wydarzenia.
    
    Przyjmuje dane przesłane przez użytkownika,
    inicjuje proces rejestracji oraz kieruje
    na odpowiedni widok w zależności od wyniku operacji.
    """
    
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        
        registration, errors = Registration.create(
            name = name,
            email = email,
        )
        
        if errors:
            return render_template(
                "register.html",
                errors = errors,
            )
        
        db.session.add(registration)
        db.session.commit()
        
        return redirect(url_for("thank_you"))
    return render_template("register.html")

@app.route("/thank-you")
def thank_you() -> str:
    return """
        <h2>Dziękujemy za rejestrację!</h2>
        <a href="/register">Wróć do formularza</a>
    """

with app.app_context():
    db.create_all()

  
if __name__ == "__main__":
    app.run(debug=True)