from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('body_setting_super/', views.change_scheme, name='change_scheme'),
    path('reset_body_setting_super/', views.reset_change_scheme, name='reset_change_scheme'),
    path('ratings_super/', views.ratings, name='ratings'),
    path('register/', views.register, name='register'),
    path('article/<int:id>/', views.article, name='article'),
    path('article/<int:id>/comment', views.comment, name='comment'),
    path('serch/', views.serch, name='serch'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
    path('add_bookmarks/<int:id>', views.add_bookmarks, name='add_bookmarks'),
    path('logout/', views.logout_user, name='logout'),
]
