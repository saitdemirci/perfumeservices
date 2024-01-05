from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns =[
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('contactform',views.contactform,name="contactform"),
    # path('login',auth_view.LoginView.as_view(template_name='registration/login.html'),name="login"),
]
