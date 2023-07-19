from django.urls import path
from .views import book_list, book_update

urlpatterns = [
    path('', book_list, name="home"),
    path('<int:pk>', book_update, name="update")
]