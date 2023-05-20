from django.urls import path
from . import views

urlpatterns = [
    path('request-self/',views.BloodRequestCreateAPIView.as_view(),name="create self"),
    path('donate-self/',views.DonateCreateAPIView.as_view(),name="donate self"),
    path('request-other/',views.BloodRequestCreateManuallyAPIView.as_view(),name="create self"),
    path('donate-other/',views.DonateCreateManuallyAPIView.as_view(),name="donate self"),
    path('<int:pk>/request-approved/',views.approved,name="approved request"),
    path('<int:pk>/request-delete/',views.deleteRequest,name = "delete request"),
    path('user/blood-requests/',views.UserBloodRequestsView.as_view(),name="user requests"),
    path('all/blood-requests/',views.BloodRequestListView.as_view(),name="all requests"),
    path('<int:pk>/donate-approved/',views.update_donation_blood_group,name="approved Donate"),
    path('<int:pk>/donate-delete/',views.deleteDonate,name = "delete donate"),
    path('user/donate-requests/',views.UserDonaterequestsView.as_view(),name="user requests"),
    path('all/donate-requests/',views.DonaterequestListView.as_view(),name="all requests"),
]

