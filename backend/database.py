from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import backend.src.models


# postgresql איך לחבר ל
# https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/#configure-the-extension

# https://flask-sqlalchemy.readthedocs.io/en/stable/config/#
db = SQLAlchemy()
# יוצר אובייקט מסוג SQLAlchemy – זה יהיה "המנהל" של החיבור למסד הנתונים ושל המודלים שלך

def init_database(app: Flask):
    # מגדיר פונקציה בשם init שמקבלת אובייקט Flask (האפליקציה שלי)
    db.init_app(app)
    # מחבר את אובייקט ה־SQLAlchemy לאפליקציית Flask כדי שיוכל להשתמש בהגדרות החיבור למסד הנתונים


def create_tables():
    # from backend.src.models.coffee_model import Coffee
    # from backend.src.models.order_model import Order
    # from backend.src.models.user_model import User

    db.create_all()


def drop_tables():
    db.drop_all()