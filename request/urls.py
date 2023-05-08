from django.urls import path
from . import views

urlpatterns = [
    path('blood/create-self/',views.BloodRequestCreateAPIView.as_view(),name="create self"),
    path('blood/create-other/',views.BloodRequestCreateManuallyAPIView.as_view(),name="create self"),
    path('blood/<int:pk>/approved/',views.approved,name="approved request"),
    path('blood/user/blood-requests/',views.UserBloodRequestsView.as_view(),name="user requests"),
    path('blood/all/blood-requests/',views.BloodRequestListView.as_view(),name="all requests"),
]
