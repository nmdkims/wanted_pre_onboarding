from django.urls import path
from .views import JobPostingsAPIView, JobPostingDetailAPIView

urlpatterns = [
    path('JobPostings/', JobPostingsAPIView.as_view()),
    path('JobPostings/<int:pk>', JobPostingDetailAPIView.as_view())
]
