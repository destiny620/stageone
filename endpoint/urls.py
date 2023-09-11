from django.urls import path
from .views import DesView



urlpatterns = [
   
    path('apidetail', DesView.as_view(), name="home")
]