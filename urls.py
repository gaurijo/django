from django.urls import path 

from . import views #from root directory import views 

urlpatterns = [
  path("", views.index, name="index")
]