from django.contrib import admin

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email')
    list_display_links = ('id','first_name','last_name')


