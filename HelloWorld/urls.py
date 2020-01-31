from django.urls import path
from . import views

app_name = "HelloWorld"

urlpatterns = [
    path("", views.resp_home, name = "home"),
    path("posts/<int:id>/", views.resp_post, name = "post"),
]