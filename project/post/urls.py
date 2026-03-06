from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='list-create-update-retrieve-destroy-post'),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-post'),
]