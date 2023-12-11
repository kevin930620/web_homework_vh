from django.contrib import admin
from .models import Member,Field

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","joined_date","age",)

admin.site.register(Member,MemberAdmin)

class FieldAdmin(admin.ModelAdmin):
    list_display = ("name","type","locate",)
admin.site.register(Field,FieldAdmin)

# admin.site.register(Field)
# Register your models here.
