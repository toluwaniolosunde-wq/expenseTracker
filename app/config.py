import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/expense_tracker"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-key"