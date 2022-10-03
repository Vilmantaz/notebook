from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('categories/', views.UserCategoriesListView.as_view(), name='categories'),
    # path('categories/', views.user_categories, name='categories'),

]