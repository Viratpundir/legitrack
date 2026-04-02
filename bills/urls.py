from django.urls import path
from .views import get_bills

urlpatterns = [
    path('bills/', get_bills),
]