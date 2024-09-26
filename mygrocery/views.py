from django.shortcuts import render, redirect
from django.http import HttpResponse
import pickle
import os
from django.conf import settings
from .predictClass import predictClass


def home(request):
    return render(request, "home.html")


def get_num_items(request):
    if request.method == "POST":
        num_items = request.POST.get("num_items")
        if num_items and int(num_items) > 0:
            # Load top_items to display them on the item input page
            pkl_file_path1 = os.path.join(settings.BASE_DIR, "model", "top_items.pkl")
            top_items = pickle.load(open(pkl_file_path1, "rb"))
            cap_items = [i.capitalize() for i in top_items]
            num_items = int(num_items)
            return render(
                request,
                "item_input.html",
                {
                    "num_items": range(1, num_items + 1),
                    "items_num": num_items,
                    "top_items": cap_items,
                },
            )
    return render(request, "num_of_items.html")


def get_items(request, items_num):
    if request.method == "POST":
        # Collect the item names from the POST data
        items = [request.POST.get(f"item_{i+1}") for i in range(int(items_num))]
        items = [item.lower() for item in items]

        # Load necessary data for prediction
        pkl_file_path2 = os.path.join(settings.BASE_DIR, "model", "all_items.pkl")
        all_items = pickle.load(open(pkl_file_path2, "rb"))
        pkl_file_path = os.path.join(settings.BASE_DIR, "model", "rules.pkl")
        rules = pickle.load(open(pkl_file_path, "rb"))

        obj = predictClass(rules)

        # Check if all items are valid
        for item in items:
            if item not in all_items:
                return render(request, "notfound.html")

        # Generate recommendations based on the input items
        item_set = set(items)
        result = obj.predict(item_set)
        cap_items = [i.capitalize() for i in result]

        return render(request, "recommend.html", {"items": cap_items})
