from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customers', views.Customers, basename="customers")


urlpatterns = [
    

   #path("",views.Customers.as_view()), # Used for Mixins,Genetics
   #path("fetch/<int:pk>/",views.CustomersDetail.as_view()), # Used for Mixins,Genetics

   path("",include(router.urls)), # Used for Viewsets

]
