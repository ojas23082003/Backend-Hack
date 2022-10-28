# todo/todo_api/views.py
# from django.utils.translation import Trans
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Profile
from .models import Order
from .models import Transaction
from .serializer import ProfileSerializer
from .serializer import OrderSerializer
from .serializer import TransactionSerializer
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from django.http import HttpResponse

class ProfileView(APIView):
    # add permission to check if user is authenticated
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
      
        user = Profile.objects.get(id = int(request.data.get('id')))
        serializer = ProfileSerializer(user)
        print("get profile",user.name)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'name': request.data.get('name'), 
            'quant': request.data.get('quant'), 
            'fiat': request.data.get('fiat'),
        }
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderView(APIView):
    # add permission to check if user is authenticated
  

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        # user = Profile.objects.filter(user = request.user.id)
        # user = Profile.objects.filter(user = request.user.id)
        order = Order.objects.all()
        serializer = OrderSerializer(order, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            # 'user': request.data.get('user'), 
            'quant1': request.data.get('quant1'), 
            'buy': request.data.get('buy'),
            'price': request.data.get('price'),
            'market': request.data.get('market'),
        }
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # populate user ield in current orde object
            user=Profile.objects.get(id=int(request.data.get('user')))
            order=Order.objects.get(id=serializer.id)
            order.user_id=user.id
            
            order.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionView(APIView):
    # add permission to check if user is authenticated
  

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            # 'buyer': request.data.get('buyer'), 
            # 'seller': request.data.get('seller'), 
            'price': request.data.get('price'),
            'quant': request.data.get('quant'),
        }
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
            buyer=Profile.objects.get(id=int(request.data.get('buyer')))
            seller=Profile.objects.get(id=int(request.data.get('seller')))
            trans=Transaction.objects.get(id=serializer.data.id)
            trans.buyer_id=buyer.id
            trans.seller_id=seller.id
            trans.save()
            # populate buye and seller ields in object
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def create_user(request):
    name = request.POST['name']
    quant = request.POST['quant']
    fiat = request.POST['fiat']

    user = User.objects.create_user(name=name, quant=quant, fiat=fiat)
    user.save()
    return HttpResponse('<h1>User added successfuly!</h1>')

def create_order(request):
    user = request.POST['user']
    quant1 = request.POST['quant1']
    buy = request.POST['buy']
    price = request.POST['price']
    type = request.POST['type']

    order = User.objects.create_order(user=user, quant1=quant1, buy=buy, price=price, type=type)
    order.save()
    return HttpResponse('<h1>User added successfuly!</h1>')    

def create_transaction(request):
    buyer = request.POST['buyer']
    seller = request.POST['seller']
    price = request.POST['price']
    quant = request.POST['quant']

    transaction = User.objects.create_transaction(buyer=buyer, seller=seller, price=price, quant=quant)
    transaction.save()
    return HttpResponse('<h1>User added successfuly!</h1>')
    