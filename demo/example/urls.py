from django.urls import path

from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path('create/', views.create_article, name='create_article'),
    path('list/', views.article_list, name='article_list'),
]
