from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
import re
from decimal import Decimal
from django.utils import timezone




def validate_expense_name(value):
   
    value =value.strip()

      # empty after removing spaces
    if not value:
        raise ValidationError("Expense name cannot be empty.")

    # Mininum length
    if len(value) <3:
        raise ValidationError("Expense name must be at least 3 characters long.")

    #cannot be only numbers
    if value.isdigit():
        raise ValidationError("Expense name cannot contain only numbers.")

    #Allow only letters, numbers,spaces, &, -, and parantheses
    if not re.fullmatch(r"[A-Za-z0-9\s&()-]+",value):
        raise ValidationError (
            "Expense name can contain only letters,numbers,& spaces,&,-, and parantheses."
        )



validate_amount = MinValueValidator(
    Decimal("0.01"),
    message="Amount must be greater than 0."
)

def validate_not_future(value):
    if value > timezone.localdate():
        raise ValidationError("Future dates are not allowed.")
        