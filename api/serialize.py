from rest_framework import serializers
from gis.models import Posisi
class PosisiSerialize(serializers.ModelSerializer):
    class Meta:
        model = Posisi
        field = ('lat', 'lang')
        