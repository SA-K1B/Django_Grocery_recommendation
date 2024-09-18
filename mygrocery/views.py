from django.shortcuts import render
from django.http import HttpResponse
import pickle
from django.http import JsonResponse
import os
import pandas as pd
from django.conf import settings
from .predictClass import predictClass
from .forms import NumItemsForm,generate_items_form
def get_num_items(request):
    if request.method == 'POST':
        form = NumItemsForm(request.POST)
        if form.is_valid():
            num_items = form.cleaned_data['num_items']
            ItemsForm = generate_items_form(int(num_items))
            print(num_items)
            form1 = ItemsForm()
            print(form1)
            return render(request, 'item_input.html', {'form': form1, 'num_items': num_items})
    else:
        form = NumItemsForm()
        return render(request, 'num_of_items.html', {'form': form})

def get_items(request, num_items):
    if request.method == 'POST':
        ItemsForm = generate_items_form(int(num_items))
        form = ItemsForm(request.POST)
        if form.is_valid():
           items = [form.cleaned_data[f'item_{i+1}'] for i in range(int(num_items))]
           pkl_file_path = os.path.join(settings.BASE_DIR, 'model', 'rules.pkl')
           rules = pickle.load(open(pkl_file_path,'rb'))
           obj = predictClass(rules)
           item_set = set(items)
           print(item_set)
           result = obj.predict(item_set)
           context = {
            'items': result
           }
           return render(request,'recommend.html',{'items':result})
    # return render(request, 'inputapp/item_input.html', {'form': form, 'num_items': num_items})
# Create your views here.
