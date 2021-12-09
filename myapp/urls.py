from django.urls import path
from .views import home,signup,login,detailview,about,cartview,itemdelete,forgotpassword,changepassword,logout

urlpatterns = [
    path('home/',home,name="home"),
    path('home/about',about,name="about"),
    path('home/signup/',signup,name="signup"),
    path('home/login/',login,name="login"),
    path('home/<int:pk>',detailview,name="detailview"),
    path('home/about',about,name="about"),
    path('home/cart/',cartview,name="cart"),
    path('home/delete/<int:pk>',itemdelete,name="delete"),
    path('home/forgotpassword/',forgotpassword,name="forgotpassword"),
    path('home/changepassword/<str:usnm>/changepassword/',changepassword,name="changepassword"),
    path('home/logout/',logout,name="logout")

]
