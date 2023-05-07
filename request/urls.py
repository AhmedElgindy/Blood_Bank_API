from django.urls import path
from . import views

urlpatterns = [
    path('blood/create-self/',views.BloodRequestCreateAPIView.as_view(),name="create self"),
    path('blood/create-other/',views.BloodRequestCreateManuallyAPIView.as_view(),name="create self"),

    path('blood-requests/<int:pk>/approved/',views.approved,name="approved request")
]
