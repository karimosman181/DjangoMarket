from django import forms
from .modesl import Item

class NewIetmForm(forms.ModelFom):
    class Meta:
        model = Item
        fields = ('category','name','description','price', 'image')
