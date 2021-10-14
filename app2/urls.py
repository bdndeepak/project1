from django.urls import path
from app2 import views

urlpatterns=[
    path('' , views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('user_signup/',views.user_signup,name='user_signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('addpost/',views.add_post,name='addpost'),
    path('update/<int:id>/',views.update_post,name='update'),
    path('deletepost/<int:id>/',views.delete_post,name='deletepost'),


]