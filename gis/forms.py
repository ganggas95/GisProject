from django import forms

class UploadFilesForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'title'}))
    files = forms.FileField(widget=forms.FileInput(attrs={'class':'hidden form-control','id':'file'}))

class Bendung(forms.Form):
    nama_bendung =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'nama_bendung'}),max_length=45)
    tahun_buat =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'tahun_buat'}),max_length=4)
    biaya = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'biaya'}))
    keterangan = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'keterangan'}),max_length=45)
    desa = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'desa'}),max_length=45)
    kec = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'kec'}),max_length=45)
    kab = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'kab'}),max_length=45)
    lang = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'lang'}))
    lat = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'lat'}))