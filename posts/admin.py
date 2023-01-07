from django.contrib import admin
from .models import posts
# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display=("id","title","desciption","create_at","update_at")
    search_fields=['title']
    list_filter=("id","title","desciption")
admin.site.register(posts,postAdmin)