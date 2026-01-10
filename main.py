

from flask import Flask, send_from_directory

# מייבא את CORS כדי לאפשר קריאות מהדפדפן ממקורות שונים
from flask_cors import CORS



from backend.database import init_database, create_tables

# מייבא את הספרייה לקריאת משתנים מקובץ .env
from dotenv import load_dotenv
import os


# טוען את משתני הסביבה מקובץ .env
load_dotenv()
server_port = int(os.getenv("SERVER_PORT"))         # פורט של השרת
server_ip = os.getenv("SERVER_IP")                  # כתובת IP של השרת
database_ip = os.getenv("DATABASE_IP")              # כתובת IP של בסיס הנתונים
DATABASE_URL = os.getenv("DATABASE_URL")            # כתובת התחברות לבסיס הנתונים

# יצירת אפליקציית Flask עם הגדרות לתיקיית קבצים סטטיים (לרוב React)
# app = Flask(__name__, static_folder='./dist', static_url_path=None)

# load_dotenv()
# flask - http פריימוורק שנותן שרת 
# routes כולל תמיכה ב 

# 1) create flask
app = Flask(__name__)

# הגדרת כתובת בסיס הנתונים עבור SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f"{DATABASE_URL}"

# ביטול מעקב אחר שינויים במודלים (משפר ביצועים)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database  חיבור ל
init_database(app)

# יצירת טבלאות אם אינן קיימות
with app.app_context():
    # drop_tables()
    create_tables()


# כאשר דפדפן שמחובר לשרת אחר שולח בקשה לשרת הזה
# headers מורה לפלאסק לשלוח כתשובה 
# חזרה לדפדפן ששלח את הבקשה
# אחרת הדפדפן חוסם את התשובה
CORS(app)

# כדי להורות לפלאסק להעביר בקשות לראוט
# app.register_blueprint(users_bp)




# נתיב ראשי שמטפל בכל הבקשות שמגיעות מהדפדפן לאפליקציית React.
# אם הבקשה היא לקובץ סטטי (כמו CSS, JS, תמונה) והוא קיים בתיקיית build — נחזיר אותו ישירות.
# אם הבקשה היא לנתיב שאינו קובץ (למשל login ), נחזיר את index.html של React,
# כדי ש־React יוכל לטפל בניווט בצד הלקוח (Client-side routing).
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def handle_react(path):
    full_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(full_path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")
    
    



# run flask
if __name__ == "__main__":
    app.run(host=server_ip, port=server_port)  # HTTP רגיל