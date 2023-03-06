from django.urls import path
from .views import UserList, FileUploadView, FileUploadViewing


urlpatterns = [
    path("", UserList.as_view(), name="user-list"),
    path("upload/", FileUploadView.as_view(), name="file-upload"),
    path("uploadering/", FileUploadViewing.as_view(), name="person_upload"),
]
