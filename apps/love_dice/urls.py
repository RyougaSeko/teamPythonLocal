from django.urls import path
from . import views

urlpatterns = [
    # path('パス', ルーティングする関数, name='urlpatternの名前'),
    path('', views.index, name='index'),
    path('edit/<int:item_id>/', views.edit_memo, name='edit_memo'),
    path('delete/<int:item_id>/', views.delete_memo, name='delete_memo'),
    path('create/', views.create_memo, name='create_memo'),
    path('memos/', views.memos, name='memos'),
]
