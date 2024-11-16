from django.shortcuts import render

# Create your views here.

from .models import SeasonalFlavour,Ingrediate,CustomerSuggestion

def show_all_data(request):
    seasonal_flavors=SeasonalFlavour.objects.all()
    ingredients = Ingrediate.objects.all()
    customer_suggestion=CustomerSuggestion.objects.all()
    return render(request,'myapp_name/flavors.html',{
        'seasonal_flavors':seasonal_flavors,
        'ingredients':ingredients,
        'customer_suggestions':customer_suggestion,
         })