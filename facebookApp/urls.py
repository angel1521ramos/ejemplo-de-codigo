from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.accounts, name='accounts'),
    path('save_accounts/', views.save_accounts, name='save_accounts'),
    path('detail_accounts/<int:accounts_id>/', views.detail_accounts, name='detail_accounts'),
    path('update_accounts/<int:accounts_id>/', views.update_accounts, name='update_accounts'),
    path('delete_accounts/<int:accounts_id>/', views.delete_accounts, name='delete_accounts'),
#
#
    #path('comments/', views.comments, name='comments'),
    #path('save_comments/', views.save_comments, name='save_comments'),
    #path('detail_comments/<int:comments_id>/', views.detail_comments, name='detail_comments'),
    #path('update_comments/<int:comments_id>/', views.update_comments, name='update_comments'),
    #path('delete_comments/<int:comments_id>/', views.delete_comments, name='delete_comments'),
#
#
    path('likes/', views.likes, name='likes'),
    path('like/<int:accounts_id>/', views.like, name='like'),
    path('shares/', views.shares, name='shares'),
    path('share/<int:accounts_id>/', views.share, name='share'),
    #path('share/', views.share, name='share'),
    #path('likes_tweets/', views.likes_tweets, name='likes_tweets'),
    #path('like_tweet/<int:accounts_id>/', views.like_tweet, name='like_tweet'),
]