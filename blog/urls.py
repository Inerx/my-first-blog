from django.urls import path
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('user_logout', views.user_logout, name='logout'),
    path('add/<int:liczba1>/<int:liczba2>/', views.add_liczby, name='adding') 
 ]
urlpatterns += staticfiles_urlpatterns()
