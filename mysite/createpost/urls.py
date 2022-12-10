from django.urls import path

from createpost import views

urlpatterns = [
    path('', views.createPost, name='userpage'),
]