from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('regsister/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),

    path('profilepage/', views.profilePage, name="profilepage"),

    path('connect4/', views.connect4, name="connect4"),
    path('snake/', views.snake, name="snake"),
    path('tictactoe/', views.tictactoe, name="tictactoe"),

    path('editprofile/', views.editProfile, name="editprofile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
