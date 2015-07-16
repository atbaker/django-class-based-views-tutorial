from django.contrib import admin

from .models import Cheese

# Register our Cheese model with the basic ModelAdmin
admin.site.register(Cheese, admin.ModelAdmin)
