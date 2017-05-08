from django.conf.urls import url
from .views import(
    maps,
    input_maps,
    bendung
)

urlpatterns = [
    url(r'^$', maps, name="maps"),
    url(r'^input_maps/', input_maps, name="input_maps"),
    url(r'^bendung/', bendung, name="bendung"),
]
