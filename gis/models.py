from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class AttrDAS(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama_das = models.CharField(max_length=45)
    kode = models.CharField(max_length=4)
    area = models.FloatField()
    perimeter = models.FloatField()

class DAS(models.Model):
    id = models.BigAutoField(primary_key=True)
    attr_id = models.ForeignKey(AttrDAS, on_delete=models.CASCADE)
    coordinates = models.BinaryField()

class Bendung(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama_bendung = models.CharField(max_length=45)
    tahun_buat =  models.CharField(max_length=4)
    biaya = models.BigIntegerField()
    keterangan = models.CharField(max_length=45)

class Lokasi(models.Model):
    id = models.BigAutoField(primary_key=True)
    desa = models.CharField(max_length=45)
    kec = models.CharField(max_length=45)
    kab = models.CharField(max_length=45)
    
    

class Posisi(models.Model):
    id =  models.BigAutoField(primary_key=True)
    lang = models.FloatField()
    lat = models.FloatField()

class DataTeknik(models.Model):
    id =  models.BigAutoField(primary_key=True)
    ca = models.FloatField()
    luas_genangan = models.FloatField()
    tipe_konstruksi = models.CharField(max_length=45)
    volume = models.BigIntegerField()
    luas = models.FloatField()
    h_sungai = models.FloatField()
    h_pondasi = models.FloatField()
    lebar_spill = models.FloatField()

class Fungsi(models.Model):
    id = models.BigAutoField(primary_key=True)
    irigasi = models.FloatField()
    ternak = models.IntegerField()
    air_baku = models.IntegerField()
    pltm = models.IntegerField()

