from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('articles/', views.getArticles, name='articles'),
    path('article/<slug:post>/', views.get_article_detail, name='article_detail'),
    # path('article/<int:year>/<int:month>/<int:day>/<slug:article>/', views.get_article_detail, name='article_detail'),
    path('scholars/', views.getScholars, name='scholars'),
    path('officers/', views.getOfficers, name = 'officers'),
    path('officer/<str:pk>/', views.getOfficer, name = 'officer'),

]