from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Chubanshe)
class ChubansheAdmin(admin.ModelAdmin):
    list_display = ['cbs_id','cbs_name','cbs_kucun']
@admin.register(Jiaocai)
class JiaocaiAdmin(admin.ModelAdmin):
    list_display = ['jc_id','jc_name','cbs_name','zuozhe','danjia']
@admin.register(Dinggou)
class DinggouAdmin(admin.ModelAdmin):
    list_display = ['jc_id','cbs_id','xx_id','dg_dgliang','dg_dhliang','dg_lyliang']
@admin.register(Xuexiao)
class XuexiaoAdmin(admin.ModelAdmin):
    list_display = ['xx_id','xx_name']

