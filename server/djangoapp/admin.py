from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)
# CarModelInline class
class CarModelInline (admin.stackedInLine):
    model = CarModel
    extra = 10

# CarModelAdmin class
Class CarModelAdmin (admin.ModelAdmin)
# CarMakeAdmin class with CarModelInline

# Register models here
