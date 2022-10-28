# backend/Chainbreakers/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    name = models.CharField(max_length=250, default='Unknown')
    quant = models.IntegerField(default=0)
    fiat = models.FloatField(default=0)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    # timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    quant1 = models.IntegerField(default=0)
    buy = models.BooleanField()
    # True==buy False==sell
    price = models.FloatField(default=0)
    market = models.BooleanField()
    # True==market order Falselimit order
    
    
    def __str__(self):
        return self.user.name  

class Transaction(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='buyer', null=True , blank=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='seller', null=True, blank=True)
    price = models.FloatField(default=0)
    quant = models.IntegerField(default=0)

    def __str__(self):
        return self.buyer + '-' + self.seller     