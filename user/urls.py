from django.urls import path
from .views import UserApiView

urlpatterns = [
    path('user/', UserApiView.as_view())
]