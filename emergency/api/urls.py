"""
Temel Alınan - Gönderilen Veri: JSON
DJANGO'da alınan-gönderilen: HTML

###################
DJANGO İŞ AKIŞI
###################

url -> view -> model -> view -> HTMLResponse

VİEW İŞ AKIŞI

data + html_file -> render() -> TemplateBackend (Django Template Language işlemelerini yapmak)

HTML FILE ÖRN:

{% for hasta in hastalar %}
<tr>
    <td> {{hasta.ad}} </td>
    <td> {{hasta.soyad}} </td>
    <td> {{hasta.yaş}} </td>
</tr>
{% endfor %}

Rest Framework
#################
data -> json
ÖRN:

Hasta Adı: Yılmaz
Hasta Soyadı: Çetin
Hasta Yaşı: 19

db_columns = first_name, last_name, year
db_table = Patient (Hasta)

{
    'first_name': 'Yılmaz',
    'last_name': 'Çetin',
    'year': 19
}

JSON TEMEL YAPISI
{
'key': 'value',
}
key'ler veritabanındaki sütun adları
value'da o sütuna karşılık verimizdir.

REST FRAMEWORK İŞ AKIŞI
############################

url -> view -> model -> serializer -> view

url -> data -> serializer -> model -> view

SERIALIZER: kendisine gelen veriyi veritabanına kaydeder. Veritabanındaki veriyi Json'a dönüştürür.

DJANGO REQUEST METODLARI: get, post
API METODLARI: get, create, delete, list, update, put, patch, post

get -> ListView
post -> DetailView
create -> CreateView
delete -> DeleteView
update -> UpdateView

ViewSet -> ListView +       DetailView +            CreateView +                        DeleteView +           UpdateView
URL'ler -> (model_name/)    (model_name/<int:pk>/)  (model_name/create + method:post)   (model_name/delete)

class ViewSet(ViewSet):
    model = Ambulance
    serializer = AmbulanceSerializer

"""

from django.urls import path

from . import views

urlpatterns = [
    path('ambulance/', views.AmbulanceListView.as_view(), name="ambulance")
]