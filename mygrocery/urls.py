from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("itemnumber", views.get_num_items, name="num_items"),
    path("items/<str:items_num>", views.get_items, name="item_input"),
]
