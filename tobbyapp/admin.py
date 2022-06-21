from django.contrib import admin
from django.urls import reverse
from .models import electrical,salon,welding

# Register your models here.

class ElectricalsAdmin(admin.ModelAdmin):
    
    list_display=(
    'itemname',
    'itemprice',
    'itemquantity',
    'totalamount'

)

admin.site.register(electrical,ElectricalsAdmin)

class SalonAdmin(admin.ModelAdmin):
    
    list_display=(
    'itemname',
    'itemprice',
    'itemquantity',
    'totalamount'

)

admin.site.register(salon,SalonAdmin)

class WeldingAdmin(admin.ModelAdmin):
    
    list_display=(
    'itemname',
    'itemprice',
    'itemquantity',
    'totalamount'

)

admin.site.register(welding,WeldingAdmin)






