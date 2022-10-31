from django.urls import path
from . import views

app_name= "account"

urlpatterns = [
   # path("account/login",views.loginView,name="login"),
   path("signup/",views.registerView,name="signup")
]
