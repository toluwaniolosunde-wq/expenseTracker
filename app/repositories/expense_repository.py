from app.models.expense import Expense
from app.database.database import db


class ExpenseRepository:

    @staticmethod
    def create_expense(expense):

        db.session.add(expense)
        db.session.commit()

        return expense


    @staticmethod
    def get_all(user_id):

        return Expense.query.filter_by(user_id=user_id).all()


    @staticmethod
    def delete_expense(expense):

        db.session.delete(expense)
        db.session.commit()