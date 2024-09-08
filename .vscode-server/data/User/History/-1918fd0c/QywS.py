from django.contrib import admin
from myapp import models
admin.site.register(models.Question)
admin.site.register(models.Answer)

# Register your models here.
