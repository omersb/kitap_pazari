from rest_framework import generics
from rest_framework.generics import get_object_or_404

from kitaplar.models import Kitap, Yorum
from kitaplar.api.serializers import KitapSerializer, YorumSerializer


class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer


class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer


class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer

    # Bir yorum yaratabilmek için bir kitap nesnesine bağlamamız lazım
    # Bu sebeple url içerisinde bir kitaba ait PK koyacağız ve buradan bu PK ile
    # ilgili kitap nesnesini çekip, yarattığımuz yoruma bağlayacağız  ==> http://127.0.0.1:8000/api/kitaplar/1/yorum_yap
    # Bu işlemleri yapabilmemiz için de perform_create metoduna müdahale etmemiz gerekiyor.
    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        serializer.save(kitap=kitap)


class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer

# class KitapListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
