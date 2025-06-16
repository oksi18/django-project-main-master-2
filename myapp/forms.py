from django import forms
from .models import Logs, Message


class Form1(forms.ModelForm):
    class Meta:
        model= Logs
        fields= ["name", "number", "action"]

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["email", "text"]