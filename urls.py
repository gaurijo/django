from django.urls import path 

from . import views #from root directory import views 

# like ruby routes.rb file 

urlpatterns = [
  path("", views.index, name="index"), 
  path("<str:name>", views.greet, name="greet"),
  # path("gauri", views.gauri, name="gauri")
]

# different urls for different views 