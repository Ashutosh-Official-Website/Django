from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'course']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
