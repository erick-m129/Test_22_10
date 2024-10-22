from django.shortcuts import render
from shop.models import Item
from django.http import HttpResponse

# Create your views here.
def index(request):
    items = Item.objects.all()
    return HttpResponse(items)
