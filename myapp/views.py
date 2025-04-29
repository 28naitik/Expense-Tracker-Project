from django.shortcuts import render, redirect
from .forms import expenseform, budgetform
from .models import Expense, Budget
import datetime
from django.db.models import Sum 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from django.conf import settings

def index(request):
    if request.method == "POST":
        if 'submit_expense' in request.POST:
            expense = expenseform(request.POST)
            if expense.is_valid():
                expense.save()
        elif 'submit_budget' in request.POST:
            budget = budgetform(request.POST)
            if budget.is_valid():
                budget.save()

    expenses = Expense.objects.all()
    budgets = Budget.objects.all().order_by('-month')
    total_expenses = expenses.aggregate(Sum('amount')) 

    
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    last_week = datetime.date.today() - datetime.timedelta(days=7)

    yearly_sum = Expense.objects.filter(date__gt=last_year).aggregate(Sum('amount'))
    monthly_sum = Expense.objects.filter(date__gt=last_month).aggregate(Sum('amount'))
    weekly_sum = Expense.objects.filter(date__gt=last_week).aggregate(Sum('amount'))

 
    daily_sums = Expense.objects.filter(date__gte=last_month).values('date').order_by('date').annotate(sum=Sum('amount'))
    categorical_sums = Expense.objects.values('category').order_by('category').annotate(sum=Sum('amount'))

    
    categories = [item['category'] for item in categorical_sums]
    sums = [item['sum'] for item in categorical_sums]
    plt.figure(figsize=(8, 6))
    plt.pie(sums, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Spread Across Categories')
    pie_chart_path = os.path.join(settings.STATICFILES_DIRS[0], 'myapp', 'charts', 'pie_chart.png')
    os.makedirs(os.path.dirname(pie_chart_path), exist_ok=True)
    plt.savefig(pie_chart_path)
    plt.close()

    
    dates = [item['date'].strftime('%Y-%m-%d') for item in daily_sums]
    sums = [item['sum'] for item in daily_sums]
    plt.figure(figsize=(8, 6))
    plt.plot(dates, sums, marker='o', color='green')
    plt.title('Daily Expenses (Last 30 Days)')
    plt.xlabel('Date')
    plt.ylabel('Amount ($)')
    plt.grid(True)
    plt.xticks(rotation=45)
    line_chart_path = os.path.join(settings.STATICFILES_DIRS[0], 'myapp', 'charts', 'line_chart.png')
    plt.savefig(line_chart_path, bbox_inches='tight')
    plt.close()

  
    today = datetime.date.today()
    current_month_budget = Budget.objects.filter(month__year=today.year, month__month=today.month).first()
    spent_this_month = Expense.objects.filter(date__year=today.year, date__month=today.month).aggregate(Sum('amount'))['amount__sum'] or 0
    budget_remaining = current_month_budget.amount - spent_this_month if current_month_budget else None

    context = {
        'expense_form': expenseform(),
        'budget_form': budgetform(),
        'expenses': expenses,
        'budgets': budgets,
        'total_expenses': total_expenses,
        'yearly_sum': yearly_sum,
        'monthly_sum': monthly_sum,
        'weekly_sum': weekly_sum,
        'daily_sums': daily_sums,
        'categorical_sums': categorical_sums,
        'pie_chart_url': 'myapp/charts/pie_chart.png',
        'line_chart_url': 'myapp/charts/line_chart.png',
        'current_month_budget': current_month_budget,
        'spent_this_month': spent_this_month,
        'budget_remaining': budget_remaining
    }
    return render(request, 'myapp/index.html', context)

def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = expenseform(instance=expense)
    if request.method == "POST":
        form = expenseform(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'myapp/edit.html', {'expense_form': expense_form})

def delete(request, id):
    if request.method == 'POST' and 'delete' in request.POST:
        Expense.objects.get(id=id).delete()
    return redirect('index')
