from rest_framework.serializers import ModelSerializer
from . import models
class StudentSerializer(ModelSerializer):
    class Meta:
        model = models.StudentModel
        fields = '__all__'