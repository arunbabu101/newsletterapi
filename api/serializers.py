from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =Item
        fields = ('__all__')


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model =Newletter
        fields = ('__all__')