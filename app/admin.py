from django.contrib import admin
from .models import files

# Register your models here.
@admin.register(files)
class filesAdmin(admin.ModelAdmin):
	list_display = ['id', 'file', 'uploaded_at']
	
