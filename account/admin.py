from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Comment

UserModel = get_user_model()


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = UserModel

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'description', 'photo', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', "groups", "user_permissions")}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('id', 'username', 'first_name', 'last_name', 'description', )
    search_fields = ('id', 'username', 'first_name', 'last_name')
    ordering = ('-date_joined',)


admin.site.register(UserModel, CustomUserAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'to', 'text')
    search_fields = ('id', 'author', 'to', 'text', )
