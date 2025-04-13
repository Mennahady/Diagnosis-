from rest_framework import serializers
from .models import Diagnosis

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['id', 'image', 'diagnosis_result']  
        read_only_fields = ['id', 'created_at']  
