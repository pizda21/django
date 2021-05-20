from rest_framework import serializers
from .models import Tasklist

class TaskListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tasklist
		fields ='__all__'