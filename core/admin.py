from django.contrib import admin

from core.models import Todo


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ["description", "is_completed", "user"]


admin.site.register(Todo, TodoAdmin)
