from django.shortcuts import render,redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import datetime

# Create your views here.
def index(request):
      if request.method =='POST':
            expense_form=ExpenseForm(request.POST)
            if expense_form.is_valid():
                  expense_form.save()
                  return redirect('index')
                  
      else:
            expense_form=ExpenseForm()
      
      
      # Calculate total expenses for the last 365 days
      last_year=datetime.date.today()-datetime.timedelta(days=365)
      data=Expense.objects.filter(date__gt=last_year)
      yearly_total=data.aggregate(Sum('amount'))['amount__sum'] or 0

      # Calculate total expenses for the last 30 days
      last_month=datetime.date.today()-datetime.timedelta(days=30)
      data=Expense.objects.filter(date__gt=last_month)
      monthly_total=data.aggregate(Sum('amount'))['amount__sum'] or 0
   

      # Calculate total expenses for the last 7 days
      last_week =datetime.date.today()- datetime.timedelta(days=7)
      data=Expense.objects.filter(date__gt=last_week)
      weekly_total=data.aggregate(Sum('amount'))['amount__sum'] or 0

      # Calculate total expenses for each day
      daily_totals=Expense.objects.values('date').annotate(total=Sum('amount')).order_by('date')
      

      # Calculate total expenses for each category
      category_totals = Expense.objects.values('category').annotate(total=Sum('amount'))

      # Retrieve all expenses in reverse chronological order
      expenses=Expense.objects.all().order_by('-date','-id')
      total_expenses= expenses.aggregate(Sum("amount"))['amount__sum'] or 0
      

      context = { 
            'expense_form': expense_form, 
            'expenses': expenses, 
            'total_expenses': total_expenses, 
            'yearly_total': yearly_total, 
            'monthly_total': monthly_total, 
            'weekly_total': weekly_total, 
            'daily_totals': daily_totals, 
            'category_totals': category_totals, 
            }
      return render(request,'expenses/dark-modern-index.html', context)
def edit(request,id):
      expense=Expense.objects.get(id=id)
      expense_form =ExpenseForm(instance=expense)
      if request.method == 'POST':
            form=ExpenseForm(request.POST,instance=expense)
            if form.is_valid():
                  form.save()
                  return redirect('index')
      return render(request,'expenses/modern-edit.html',{'expense_form':expense_form})

def delete(request,id):
      if request.method =='POST':
            expense =Expense.objects.get(id=id)
            expense.delete()
     
      return redirect('index')
