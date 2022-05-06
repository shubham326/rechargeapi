from django.contrib import admin
from .models import *

# Register your models here.
class planAdmin(admin.ModelAdmin):    
    list_display = [ 'id','rupees','operator','region','data','validity']

class OperatorAdmin(admin.ModelAdmin):    
    list_display = ['id','name']

class RegionAdmin(admin.ModelAdmin):    
    list_display = ['id','operator','rname']

class rechargeAdmin(admin.ModelAdmin):    
    list_display = ['id','mobile','price','Plan']

admin.site.register(plan,planAdmin)
admin.site.register(Operator,OperatorAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(recharge,rechargeAdmin)
