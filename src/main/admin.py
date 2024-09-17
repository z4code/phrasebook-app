from django.contrib import admin
from django.contrib.auth.models import Group
from . import models

admin.site.register(models.Category)
admin.site.register(models.Language)
admin.site.register(models.Phrase)

admin.site.unregister(Group)