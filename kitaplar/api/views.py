from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from kitaplar.models import Kitap
from kitaplar.api.serializers import KitapSerializer, YorumSerializer


class KitapListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
