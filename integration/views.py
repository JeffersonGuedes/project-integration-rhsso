from .serializers import NomeSerializer
from .models import Nome
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class NomeView(ModelViewSet):
    serializer_class = NomeSerializer
    queryset = Nome.objects.all()
    
