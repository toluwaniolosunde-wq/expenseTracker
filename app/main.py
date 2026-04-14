from flask import Flask
from app.database.database import db
from app.routers.auth_router import auth_router
from app.routers.expense_tracker_router import expense_tracker_router

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@localhost/expense_tracker"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

app.register_blueprint(auth_router, url_prefix="/api")
app.register_blueprint(expense_tracker_router, url_prefix="/api")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)