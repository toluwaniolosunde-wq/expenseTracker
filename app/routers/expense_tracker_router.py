from flask import Blueprint, request, jsonify
from app.schemas.expense_schema import ExpenseCreateSchema;
from app.services.expense_tracker_service import ExpenseTrackerService


expense_tracker_router = Blueprint("auth", __name__)

@expense_tracker_router.route("/expenses", methods=["POST"])
def create_expense():

    data = ExpenseCreateSchema(**request.json)

    user_id = request.json.get("user_id")

    expense = ExpenseTrackerService.create_expense(data, user_id)

    return jsonify({"message": "Expense created", "id": expense.id})


@expense_tracker_router.route("/expenses/<int:user_id>", methods=["GET"])
def get_expenses(user_id):

    expenses = ExpenseTrackerService.get_expenses(user_id)

    result = []

    for e in expenses:

        result.append({
            "id": e.id,
            "amount": e.amount,
            "category": e.category,
            "description": e.description
        })

    return jsonify(result)