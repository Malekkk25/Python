from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.index, name='articles'),
    path('articles/del_art/<int:id>', views.del_art, name='del_art'),
    path('categories/', views.list_cat, name='categories'),
    path('articles/update_art/<int:id>', views.update_art, name='update_art'),
    path('articles/update_art/update_art_action/<int:id>', views.update_art_action, name='update_art_action'),
    path('articles/addArticle/', views.add, name='add'),
    path('articles/addArticle/add_art/', views.add_art, name='add_art'),
    path('users/', views.list_users, name='users'),
    path('users/createUser/', views.create_compte, name='create_compte'),
    path('users/createUser/add_user_action/', views.create_user_action, name='create_user_action'),
    path('users/del_user/<int:id>', views.del_user, name='del_user'),
    path('users/update_user/<int:id>', views.update_user, name='update_user'),
    path('users/update_user/update_user_action/<int:id>', views.update_user_action, name='update_user_action'),
    path('', views.connect, name='connect'),
    path('login/', views.signIn, name='signIn'),
    path('login/login/', views.signIn, name='signIn'),
    path('disconnect/', views.signOut, name='disconnect')

]