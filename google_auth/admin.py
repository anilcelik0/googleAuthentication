from django.contrib import admin
from .models import photo_share

# Register your models here.

class photo_shares_admin(admin.ModelAdmin):
    list_display=("id","yt","name","photo","user")
    search_fields=("id",)
    
    
admin.site.register(photo_share,photo_shares_admin)