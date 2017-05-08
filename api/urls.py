from django.conf.urls import url
from .views import Posisi
urlpatterns = [
    url(r'^pip/', Posisi.as_view),
]