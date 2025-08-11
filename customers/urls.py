from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customers',views.Customer,basename="customers")

urlpatterns = [
   path("",views.Customer.as_view())
]
