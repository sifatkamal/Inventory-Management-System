from django.urls import path

from . import views

urlpatterns= [

    path("", views.base, name="base"),

    path("index/", views.index, name="index"),

    path("signin/", views.signin, name="signin"),

    path("signup/", views.signup, name="signup"),

    path("signout/", views.signout, name="signout"),

]