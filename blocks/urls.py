from django.urls import path
from . import views

urlpatterns = [
    path(
        'blocks/',
        views.BlockUserList.as_view(),
        name='block-list'
    ),
    path(
        'blocks/<int:pk>/',
        views.BlockUserDetail.as_view(),
        name='block-detail'
    ),
]

