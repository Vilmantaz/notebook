from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('categories/', views.UserCategoriesListView.as_view(), name='categories'),
    path('categories/new', views.UserCategoriesCreate, name='categories-new'),

]