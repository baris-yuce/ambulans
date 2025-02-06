from django.urls import path, include

app_name = 'emergency' # {% url 'app_name:url_name' %}

urlpatterns = [
    path('api/', include('emergency.api.urls'))
]


# {% url 'url_name' %}