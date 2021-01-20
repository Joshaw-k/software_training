from django.urls import path
from software_training_app import views
urlpatterns = [
    path('',views.home,name="home"),
    path('about-us',views.about_us,name="about_us"),
    path('team-detail',views.team_detail,name="team_detail"),
    path('service-detail',views.service_detail,name="service_detail"),
    path('teacher',views.teacher,name="teacher"),
    path('menu',views.menu,name="menu"),
    path('blog',views.blog,name="blog"),
    path('team',views.team,name="team"),
    path('gallery',views.gallery,name="gallery"),
]
