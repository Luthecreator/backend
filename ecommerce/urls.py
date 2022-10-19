from django.urls import path
from .views import buyProducts

urlpatterns = [
    path("item/",buyProducts)
]

