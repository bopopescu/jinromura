from django.urls import path

from . import views

urlpatterns = [
    #検索画面
    path('', views.index, name='index'),
    #村の詳細画面
    path('<int:village_id>/', views.detail, name='detail'),
]
