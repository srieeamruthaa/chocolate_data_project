from django.db import models

# Create your models here.

class SeasonalFlavour(models.Model):
    name=models.CharField(max_length=100)
    about=models.TextField()
    is_available=models.BooleanField(default=True)
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self) :
        return self.name

class Ingrediate(models.Model):
    name=models.CharField(max_length=100)
    quantity =models.IntegerField()
    unit=models.CharField(max_length=50)
    allergy_warning=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
class CustomerSuggestion(models.Model):
    flavour=models.ForeignKey(SeasonalFlavour,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=100)
    suggestion =models.TextField()
    allergies=models.TextField(null=True,blank=True)
    suggestion_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name}-{self.flavour.name}"