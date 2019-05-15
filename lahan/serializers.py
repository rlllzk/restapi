from .models import area
from rest_framework import serializers

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = area
        fields = '__all__' #kabeh /('provinsi','luas','tahun')