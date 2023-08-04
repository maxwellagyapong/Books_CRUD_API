from django.urls import path, include
# from .views import book_list, book_detail
from .views import BookVS
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', BookVS, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    # path('', book_list, name="book-list"),
    # path('<int:pk>', book_detail, name="book-detail")
]