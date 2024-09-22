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
            # print(num_items)
            form1 = ItemsForm()
            # print(form1)
            pkl_file_path1 = os.path.join(settings.BASE_DIR, 'model', 'top_items.pkl')
            top_items = pickle.load(open(pkl_file_path1,'rb'))
            cap_items=[]
            for i in top_items:
              cap_items.append(i.capitalize())
            # print(top_items)
            return render(request, 'item_input.html', {'form': form1, 'num_items': num_items,'top_items':cap_items})
    else:
        form = NumItemsForm()
        return render(request, 'num_of_items.html', {'form': form})

def get_items(request, num_items):
    if request.method == 'POST':
        ItemsForm = generate_items_form(int(num_items))
        form = ItemsForm(request.POST)
        if form.is_valid():
           items = [form.cleaned_data[f'item_{i+1}'] for i in range(int(num_items))]
           pkl_file_path2 = os.path.join(settings.BASE_DIR, 'model', 'all_items.pkl')
           all_items = pickle.load(open(pkl_file_path2,'rb'))
           pkl_file_path = os.path.join(settings.BASE_DIR, 'model', 'rules.pkl')
           rules = pickle.load(open(pkl_file_path,'rb'))
           obj = predictClass(rules)
        #    print(type(items))
           lowercase_items=[]
           for i in items:
             lowercase_items.append(i.lower())
           for i in lowercase_items:
            if i not in all_items:
                return render(request,'notfound.html')  
           item_set = set(lowercase_items)
        #    print(item_set)
           result = obj.predict(item_set)
           cap_items=[]
           for i in result:
             cap_items.append(i.capitalize())
           context = {
            'items': cap_items
           }
           return render(request,'recommend.html',context)
    # return render(request, 'inputapp/item_input.html', {'form': form, 'num_items': num_items})
# Create your views here.
