from django.urls import path
from .views import DesView

urlpatterns = [
    path('api', DesView.as_view(), name="api-detail")
]