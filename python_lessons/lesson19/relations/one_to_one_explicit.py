from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///one_to_one.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    
    profile = db.relationship(
        "Profile",
        backref="user",
        uselist=False, # 1:1
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<User {self.email}>"
    
    
class Profile(db.Model):
    __tablename__ = "profiles"
    
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=True, # wymusza 1:1 na poziomie DB
        nullable=False
    )
    
    full_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    avatar_url = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    
    def __repr__(self):
        return f"<Profile {self.full_name}>"
    
    

def db_init():
    db.create_all()
    
    if not User.query.first():
        
        user = User(
            email="jan@example.com",
            password_hash="hashed_password"
        )
        profile = Profile(full_name="Jan Kowalski",
                            bio="Python developer",
                            phone="123456789")
        user.profile = profile
        db.session.add(user)
        db.session.commit()
        
        
@app.route("/")
def index():
    
    user = User.query.filter_by(email="jan@example.com").first()
    
    output = f"""
        User: {user.email},
        Profile:
        - name: {user.profile.full_name}
        - bio: {user.profile.bio}
        - phone: {user.profile.phone}
    """
    
    return f"<pre>{output}</pre>"




if __name__ == "__main__":
    with app.app_context():
        db_init()
        
    app.run(debug=True)