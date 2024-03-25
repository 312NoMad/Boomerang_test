from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('password',)
    readonly_fields = ('id', 'created_at', 'updated_at', 'last_login', 'is_superuser')
