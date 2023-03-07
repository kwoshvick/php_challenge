from django.urls import path
from .views import UserList, FileUploadView, FileListView


urlpatterns = [
    path("", UserList.as_view(), name="user-list"),
    path("files/", FileListView.as_view(), name="file-list"),
    path("upload/", FileUploadView.as_view(), name="file-upload"),
]
