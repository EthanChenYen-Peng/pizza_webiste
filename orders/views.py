from django.shortcuts import render
from .models import Food
# Create your views here.


def index(request):
    return render(request, "orders/index.html")


def menu(request):
    #  listings = Listing.objects.order_by(
    #      '-list_date').filter(is_published=True)
    foods = Food.objects.all()
    return render(request, "orders/menu.html", {'foods': foods})


def contact(request):
    return render(request, "orders/contact.html")
