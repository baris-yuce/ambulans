from rest_framework import generics

from emergency import models
from . import serializers

class AmbulanceListView(generics.ListAPIView):
    queryset = models.Ambulance.objects.all()
    serializer_class = serializers.AmbulanceSerializer

"""
DJANGO İŞ AKIŞI

request -> form -> model -> db
db -> model -> view -> html -> response

RESTFRAMEWORK İŞ AKIŞI
request (JSON) -> serializer -> model -> db
db -> model -> serializer -> JSON Data -> View -> JSONResponse

VİEWSET

API İŞ AMAÇLARI
CRUD -> Create, Update, Detail, Select
(Django) -> CreateView, ListView, DetailView, UpdateView
ViewSet + Serializer -> CRUD işlemlerinin tamamını yapar.
ViewSet = create/ , list/ , detail/ , update/ , delete/ URL'leri için viewların hepsi bir aradadır.
urlpatterns = [
    path('list/', ListView),
    path('detail/', DetailView)
]
--------------------
SORU
--------------------
urlpatterns = [
    path('list/', ViewSet),
    path('detail/', ViewSet)
] bu şekilde mi yazmak lazım?

ÇÖZÜM
----------------
Router -> ViewSet için otomatik bir şekilde URL'leri oluştur.

router = DefaultRouter
router.register(ViewSet)
urlpatterns = router.urls

REST FRAMEWORKLE ÇALIŞIRKEN 3 ANA KOMPONENT:
Serializer -> her model için bir tane
ViewSet -> her serializer için bir tane
Router -> bir api uygulaması için bir tane (tercihen)
    her viewset register edilir.
"""