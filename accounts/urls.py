from django.urls import path
from . import views 
urlpatterns = [
    path('',views.getData,name="getData"),
    path('singup/',views.SingUp.as_view(),name="signUp"),
    path('login/',views.Login.as_view(),name="login"),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('isadmin/', views.isadmin, name="isadmin"),
    path('getuser/',views.getUserProfile,name="getuserprofile")
    ]