from django.urls import path
from . import views

urlpatterns = [
    path(
        'blocks/',
        views.BlockList.as_view(),
        name='block-list'
    ),
    path(
        'blocks/<int:pk>/',
        views.BlockDetail.as_view(),
        name='block-detail'
    ),
]

