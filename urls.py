from django.urls import path

from . import views


urlpatterns = [

    path("", views.index, name="index"),

    path("", views.project_detail, name="portfolio-details"),

]