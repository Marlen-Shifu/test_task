import rest_framework.serializers
from rest_framework.serializers import ModelSerializer

from .models import Worker


class WorkerSerializer(ModelSerializer):

    class Meta:
        model = Worker
        fields = ('id', 'full_name', 'post', 'salary', 'chief')
