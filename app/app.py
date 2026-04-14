from flask import Flask
from database import db
from routers.auth_router import auth_router
from routers.expense_tracker_router import expense_tracker_router


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expense.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

app.register_blueprint(auth_router, url_prefix="/api")
app.register_blueprint(expense_tracker_router, url_prefix="/api")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)