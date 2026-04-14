from pydantic import BaseModel
from datetime import date


class ExpenseCreateSchema(BaseModel):

    amount: float
    category: str
    description: str
    date: date