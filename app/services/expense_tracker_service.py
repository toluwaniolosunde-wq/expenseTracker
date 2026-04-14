from app.models.expense import Expense;
from app.repositories.expense_repository import ExpenseRepository;


class ExpenseTrackerService:

    @staticmethod
    def create_expense(data, user_id):

        expense = Expense(
            amount=data.amount,
            category=data.category,
            description=data.description,
            date=data.date,
            user_id=user_id
        )

        return ExpenseRepository.create_expense(expense)


    @staticmethod
    def get_expenses(user_id):

        return ExpenseRepository.get_all(user_id)