from django.urls import path
from pages import views

urlpatterns = [
    # path("", views.home, name='home'),
    path("", views.asteroids, name='asteroids'),
    path("get_data", views.api, name='api')
]
