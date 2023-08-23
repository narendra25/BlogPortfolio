from django.urls import path
from authapp import views
urlpatterns = [
    path('signup/',views.signup),
    path('login/',views.handlelogin),
    path('logout/',views.handlelogout),
]