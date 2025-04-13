from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Diagnosis
from .serializers import DiagnosisSerializer  # Correct import path

class UploadImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = DiagnosisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DiagnosisHistoryView(APIView):
    def get(self, request, *args, **kwargs):
        diagnoses = Diagnosis.objects.all().order_by('-created_at')  # Order by latest first
        serializer = DiagnosisSerializer(diagnoses, many=True)
        return Response(serializer.data)
