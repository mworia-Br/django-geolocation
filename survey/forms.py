from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from models import Data
from crispy_forms.layout import Field, Layout, Div, ButtonHolder, Submit


class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = "__all__"