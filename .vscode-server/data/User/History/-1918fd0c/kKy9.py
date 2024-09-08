from django.contrib import admin
from myapp import models

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Answer)

# Register your models here.
