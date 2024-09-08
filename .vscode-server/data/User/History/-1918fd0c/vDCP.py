from django.contrib import admin
from myapp import models

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['questionid']    

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Answer, AnswerAdmin)

# Register your models here.
