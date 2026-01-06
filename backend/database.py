from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# postgresql איך לחבר ל
# https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/#configure-the-extension

# https://flask-sqlalchemy.readthedocs.io/en/stable/config/#
db = SQLAlchemy()
# יוצר אובייקט מסוג SQLAlchemy – זה יהיה "המנהל" של החיבור למסד הנתונים ושל המודלים שלך

def init(app: Flask):
    # מגדיר פונקציה בשם init שמקבלת אובייקט Flask (האפליקציה שלי)
    db.init_app(app)
    # מחבר את אובייקט ה־SQLAlchemy לאפליקציית Flask כדי שיוכל להשתמש בהגדרות החיבור למסד הנתונים
