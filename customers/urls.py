from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('customers', views.Customers, basename="customers")


urlpatterns = [
    

   #path("",views.Customers.as_view()), # Used for Mixins,Genetics
   #path("fetch/<int:pk>/",views.CustomersDetail.as_view()), # Used for Mixins,Genetics

   #path("",include(router.urls)), # Used for Viewsets and ModelViewSet

   path("blogs/",views.Blogs.as_view()),
   path("comments/",views.Comments.as_view()),
   path("bdetail/<int:pk>/",views.BlogDetail.as_view()),
   path("cdetail/<int:pk>/",views.CommentDetail.as_view()),

]
