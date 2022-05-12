from .models import Client
from django import forms
from crispy_forms.helper import FormHelper

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        