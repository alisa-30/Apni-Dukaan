from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="home-page"),
    path("contact",views.contact,name="contact"),
    path("login", views.log_in, name="login"),
    path("contacts",views.contacts,name="contacts"),
]