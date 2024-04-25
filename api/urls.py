from django.urls import path
from .views import *

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('news/', NewsList.as_view()),
    path('news/<int:pk>/', NewsDetail.as_view()),
]
