from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from . import forms
import random, string, os
import logging
import folium
import shapefile
from json import dumps
from .models import (
    AttrDAS, DAS,Bendung, Posisi, Lokasi,  Fungsi, DataTeknik
)
def maps(request):
    return render(request, "maps.html", None)

def input_maps(request):
    form = forms.UploadFilesForm(request.POST or None, request.FILES or None)
    context = {"form" : form}
    if request.method == 'GET':
        return render(request, 'input-form.html', context)
    if request.method == 'POST':
        if form.is_valid():
            file = request.FILES['files']
            upload_file_handler(file)
            shp = str.split(file.name, ".")
            shpfile = open('temp/'+shp[0]+".shp", 'rb')
            dbffile = open('temp/'+shp[0]+".dbf", 'rb')
            shpobj = shapefile.Reader(shp=shpfile, dbf=dbffile)
            fields = shpobj.fields[1:]
            field_names = [field[0] for field in fields]
            # for sr in shpobj.shapeRecords():
            #     logging.warning(sr.record)
            buffer = []
            for sr in shpobj.shapeRecords():               
                 atr = dict(zip(field_names, sr.record))
                 geom = sr.shape.__geo_interface__
                 logging.warning(atr)
                 buffer.append(dict(type="Feature", \
                                    geometry=geom, properties=atr))
            logging.warning(buffer)
            jsonFormat = dumps({
                "type": "FeatureCollection", 
                "features": buffer
            }, indent=2)
            shp2geojson(jsonFormat, shp)
            return HttpResponseRedirect('/test/')
        return render(request, 'input-form.html', context)


def pip(x,y, poly):
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x,p2y
    logging.warning(inside)
    return inside

def upload_file_handler(f):
    logging.warning(f.name)
    with open('temp/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def shp2geojson(buffer, filename):
    # logging.warning(buffer)
    with open("temp/"+filename[0]+".json", "wb+") as geojson:
        geojson.write(buffer.encode(encoding='utf_8'))
        geojson.close()

def bendung(request):
    form_bendung = forms.Bendung(request.POST or None, request.FILES or None)
    context = {
        "form" : form_bendung,
    }
    if request.method == "GET":
        return render(request, 'add.bendung.html', context)