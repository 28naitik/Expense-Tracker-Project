from django.db import models

# Create your models here.

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Budget(models.Model):
    month = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return f"Budget for {self.month.strftime('%B %Y')}"

