from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('categories/', views.CategoriesListView.as_view(), name='categories'),
    path('categories/new', views.UserCategoriesCreate, name='categories-new'),
    path('categories/records/new', views.RecordCreateView.as_view(), name='record-new'),
    path('categories/<int:pk>', views.RecordsListView.as_view(), name='categorie_records'),
    path('categories/<int:pk>/update', views.CategoryUpdateView.as_view(), name='user-category-update'),

]