from django import forms


# Form to input the number of items
class NumItemsForm(forms.Form):
    num_items = forms.IntegerField(label="Enter a number:", min_value=1)


# Dynamic form based on the number of items
def generate_items_form(n):
    class ItemsForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(ItemsForm, self).__init__(*args, **kwargs)
            for i in range(n):
                field_name = f"item_{i+1}"
                self.fields[field_name] = forms.CharField(
                    label=f"Item {i+1}", max_length=100
                )

    return ItemsForm
