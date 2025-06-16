from django.contrib import admin
from .models import Cabinets, Logs, Message

admin.site.register(Cabinets)
admin.site.register(Logs)
admin.site.register(Message)