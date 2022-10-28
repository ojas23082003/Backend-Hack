# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Order, Profile, Transaction
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["name","quant","fiat"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user","quant1","buy","price","market"]

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["buyer","seller","price","quant"]
