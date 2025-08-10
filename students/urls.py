from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("view/",views.StudentView),
    path("fetch/<int:pk>/",views.StudentDetailView),
    path("add/",views.add,name='add'),
    path("update/<int:pk>/",views.update,name='update'),
    path("delete/<int:pk>/",views.delete,name='delete'),
]
