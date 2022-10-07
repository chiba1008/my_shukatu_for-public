from django.urls import path
from . import views
from .views import signup_func, login_func, logout_func


app_name = 'account'

urlpatterns = [
    path('signup/', signup_func, name="signup"),
    path('login/', login_func, name="login"),
    path('logout/', logout_func, name="logout"),

]