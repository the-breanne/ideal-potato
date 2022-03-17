from django.contrib import admin
from .models import Task, Feedback, Meeting

class TaskList(admin.ModelAdmin):
    list_display = ('task_number', 'name', 'city', 'cell_phone')
    list_filter = ('task_number', 'name', 'city')
    search_fields = ('task_number', 'name')
    ordering = ['task_number']


class FeedbackList(admin.ModelAdmin):
    list_display = ('task', 'category', 'description', 'recent_value')
    list_filter = ('task', 'category')
    search_fields = ('task', 'category')
    ordering = ['task']


class MeetingList(admin.ModelAdmin):
    list_display = ('task','symbol', 'name', 'shares', 'purchase_price')
    list_filter = ('task','symbol', 'name')
    search_fields = ('task','symbol', 'name')
    ordering = ['task']


admin.site.register(Task, TaskList)
admin.site.register(Feedback, FeedbackList)
admin.site.register(Meeting, MeetingList)
