from django.contrib import admin
from .models import *


admin.site.register(MetaTags)


class PostImageAdmin(admin.StackedInline):
    model = ObjectImages


@admin.register(Objects)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Objects
