from django.urls import path
from . import views 
urlpatterns = [
    path('',views.getData,name="getData"),
    path('singup/',views.SingUp.as_view(),name="signUp"),
    path('login/',views.Login.as_view(),name="login")
]