from app import db
from app.models import User
from app import app

# Создание таблиц, если они не существуют
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)