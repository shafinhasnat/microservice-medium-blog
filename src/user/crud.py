from src import db
from src.models import Users

def register(username, email):
    users = Users(username=username, email=email)
    db.session.add(users)
    db.session.commit()
    
