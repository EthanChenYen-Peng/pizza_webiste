from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="orders_index"),
    path("menu", views.menu, name="orders_menu"),
    path("contact",views.contact ,name="orders_contact")
]
