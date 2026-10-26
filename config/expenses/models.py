from django.db import models
from .validators import validate_expense_name, validate_amount,validate_not_future

from django.utils import timezone



# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100,
    validators=[validate_expense_name]
    )
    


    CATEGORY_CHOICES = [
        ("Food", "Food"),
        ("Transport", "Transport"),
        ("Shopping", "Shopping"),
        ("Bills", "Bills & Utilities"),
        ("Rent", "Rent / Housing"),
        ("Healthcare", "Healthcare"),
        ("Entertainment", "Entertainment"),
        ("Education", "Education"),
        ("Travel", "Travel"),
        ("Groceries", "Groceries"),
        ("Personal Care", "Personal Care"),
        ("Insurance", "Insurance"),
        ("EMI", "EMI / Loans"),
        ("Salary", "Salary"),
        ("Investment", "Investment"),
        ("Gift", "Gift"),
        ("Other", "Other"),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[validate_amount],
    )
      
    #date = models.DateField(auto_now=True)
    

    date = models.DateField(
    default=timezone.now,
    validators=[validate_not_future]
)

    def __str__(self):
        return self.name

   