from django.db import models
from django.contrib.auth.models import User

class UserLibraryAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    initial_deposite_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(null=True, blank=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    
    def __str__(self):
        return str(self.account_no)
    