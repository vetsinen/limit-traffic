from django.contrib import admin

from .models import User, Company, Transfer
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Transfer)