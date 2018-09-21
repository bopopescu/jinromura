from django.urls import path

from . import views

urlpatterns = [
    #検索画面
    path('', views.IndexView.as_view(), name='index'),
    #村の詳細画面
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
