from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Payment)
admin.site.register(AccountHolder)
admin.site.register(Appointment)