from django.urls import path
from . import  views
urlpatterns=[
    path('',views.get_num_items,name="num_items"),
    path('items/<str:num_items>',views.get_items,name="item_input"),
]