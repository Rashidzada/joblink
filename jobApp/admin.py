from django.contrib import admin
from .models import*
# Register your models here.
class AdminAuthor(admin.ModelAdmin):
   class Meta:
       model = Author()
       fields = ["name","email"]
admin.site.register(Author,AdminAuthor)
admin.site.register(Book)