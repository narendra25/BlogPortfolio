from django.urls import path
from portfolio import views
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('blog/',views.handleblog)
]