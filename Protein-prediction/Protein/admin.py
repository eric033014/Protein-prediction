from django.contrib import admin
from Protein.models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name','email','comment')
admin.site.register(Profile,ProfileAdmin)
