from django.forms import ModelForm
from .models import Expense, Budget
class expenseform(ModelForm):
    class Meta:
        model  = Expense
        fields = ('name','amount','category')


class budgetform(ModelForm):
    class Meta:
        model = Budget
        fields = ('month', 'amount')

