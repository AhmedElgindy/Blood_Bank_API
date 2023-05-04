from django.urls import path
from . import views

urlpatterns = [
    path('blood/create/',views.BloodRequestCreateAPIView.as_view(),name="Test"),
    path('blood-requests/<int:pk>/approved/',views.approved,name="approved request")
]
