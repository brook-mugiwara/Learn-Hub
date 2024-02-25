from django.urls import path,re_path
from . import views

urlpatterns = [
    path("home/",               views.home_page,    name='home'),
    path("player/id=<str:id>/", views.player_page,  name='player'),
    path('courses/',            views.course_page,  name='courses'),
    path('change_video/',       views.change_video, name='change_video'),
    path('next_video/',         views.next_video,   name='next_video'),
    path('quiz/',               views.quiz,         name='quiz'),
]