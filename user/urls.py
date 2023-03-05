from django.urls import path
from .views import UserList, UserUploadAPIView


urlpatterns = [
    path("", UserList.as_view(), name="user-list"),
    path("upload/", UserUploadAPIView.as_view(), name="person_upload"),
]
