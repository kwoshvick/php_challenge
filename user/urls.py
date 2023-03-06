from django.urls import path
from .views import UserList, FileUploadView


urlpatterns = [
    path("", UserList.as_view(), name="user-list"),
    path("upload/", FileUploadView.as_view(), name="file-upload"),
]
