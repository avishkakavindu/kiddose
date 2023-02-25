from django.urls import path

from api.api_views import EmotionDetectionAPIView

urlpatterns = [
 path('emotion-detection/', EmotionDetectionAPIView.as_view(), name='emotion_detection'),
]
