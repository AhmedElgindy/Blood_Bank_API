from django.urls import path
from . import views

urlpatterns = [
    path('blood/create/',views.BloodRequestCreateAPIView.as_view(),name="Test")
]
