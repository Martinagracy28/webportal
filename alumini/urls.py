from django.urls import path
from . import views

urlpatterns = [
    path("",views.base,name="base"),
    path('register',views.register, name ='register'),
    path("login",views.login, name="login"),
    path("logout",views.logout, name = "logout"),
    path('posts',views.posts, name ='posts'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('newpost/<str:pk>/',views.newpost, name='newpost'),
    path('viewing/<str:pk>/',views.viewing, name='viewing'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name = 'delete'),
    path('view/<str:pk>/',views.view, name ='view'),
    path('edit/<str:pk>/',views.edit, name ='edit'),
    path('newprofile/<str:pk>/',views.newprofile, name ='newprofile'),
  
    
]