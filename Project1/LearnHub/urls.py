from django.urls import path
from . import views

urlpatterns = [
    path("home/",   views.home_page),
    path("player/", views.player_page,name='player'),
    path('courses/',views.course_page,name='courses'),
    path('print/',  views.print)
]