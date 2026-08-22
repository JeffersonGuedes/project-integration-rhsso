from django.urls import path
from .views import NomeView

urlpatterns = [
    path('nomes/', NomeView.as_view({'get': 'list', 'post': 'create'}), name='nome-list'),
]