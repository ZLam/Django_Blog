from django.contrib import admin
from . import models

# Register your models here.

class Post_Admin(admin.ModelAdmin):
    list_display = ["title", "author", "time_create", "time_modify", "category"]
    fields = ["title", "content", "excerpt", "category", "tags"]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Post, Post_Admin)