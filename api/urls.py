from django.urls import path
from .views import UserList

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view()),
    path('', UserList.as_view()),
]
