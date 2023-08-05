from django import forms
from .models import MyModel,Image


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['image', 'cropping']



class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
