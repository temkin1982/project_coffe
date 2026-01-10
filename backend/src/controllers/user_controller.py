from backend.src.models.user_model import User
from backend.database import db
from sqlalchemy import select


def add_user(user: User):
    # Проверяем, существует ли пользователь
    existing = db.session.query(User).filter_by(user_id = user.user_id).first()

    if existing:
        raise ValueError("User already exists")

    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    return user


def user_login(email_login: str, password_login: str):
    user_login = db.session.query(User).filter(User.email == email_login, User.password == password_login).first()

    if user_login:
        return user_login
    else:
      raise ValueError("The password or email is incorrect")  



def user_from_dict(user: dict):
    return User.from_dict(user)


def user_to_dict(user: User):
    return user.to_dict()