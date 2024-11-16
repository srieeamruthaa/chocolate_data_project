from django.contrib import admin

# Register your models here.
from .models import SeasonalFlavour , Ingrediate , CustomerSuggestion

admin.site.register(SeasonalFlavour)
admin.site.register(Ingrediate)
admin.site.register(CustomerSuggestion)
