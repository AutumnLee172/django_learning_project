from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/details/<int:id>', views.details, name='details'),
    path('api/register', views.UserApiView.as_view()),
    path('api/login', views.UserLoginApi.as_view()),
]