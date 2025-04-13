from django.urls import path 
from .views import UploadImageView, DiagnosisHistoryView

urlpatterns = [
    path('upload/', UploadImageView.as_view(), name='upload-image'),
    path('history/', DiagnosisHistoryView.as_view(), name='diagnosis-history'),
]
