from django.contrib import admin
from .models import AnthemAsset,AnthemUser
# Register your models here.

admin.site.register(AnthemUser)
admin.site.register(AnthemAsset)