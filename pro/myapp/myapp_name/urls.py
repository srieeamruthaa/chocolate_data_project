from django.urls import path 
from . import views

urlpatterns=[
    path('flavors/',views.show_all_data,name='show_all_data'),
]