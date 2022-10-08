from django import forms
from django.forms import ModelForm
from .models import EsPost

class EsForm(ModelForm):
    class Meta:
        widgets = {
            'title': forms.Textarea(
                attrs={
                    "class":"form-control",
                    "rows":"1",
                }
                ),
            'content': forms.Textarea(
                attrs={
                    "class":"form-control",
                    "rows":"5",
                    "onkeyup":"ShowLength(value);"
                }
                )
        }
        model = EsPost
        exclude = ['user']
        fields = ['title', 'content']
        
        