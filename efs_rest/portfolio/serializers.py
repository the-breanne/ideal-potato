from rest_framework import serializers
from .models import Task, Feedback, Meeting


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
            model = Task

            fields = ('pk','name', 'address','task_number', 'city', 'state', 'zipcode', 'email', 'cell_phone')

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
            model = Feedback
            fields = ('pk','task', 'task_number', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value', 'recent_date')


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
            model = Meeting
            fields = ('pk','task', 'task_number', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date')
