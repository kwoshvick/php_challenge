from django.urls import path
from .views import UserList, UserUploadAPIView, FileUploadView, FileUploadViewing


urlpatterns = [
    path("", UserList.as_view(), name="user-list"),
    path("upload/", UserUploadAPIView.as_view(), name="users_upload"),
    path("uploader/", FileUploadView.as_view(), name="person_upload"),
    path("uploadering/", FileUploadViewing.as_view(), name="person_upload"),
]
