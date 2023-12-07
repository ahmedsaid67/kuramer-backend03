from rest_framework import serializers
from .models import Slider

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')




class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


from .models import Menu, MenuItem

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = '__all__'


# Personel

from .models import PersonelTuru

class PersonelTuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonelTuru
        fields = ['id', 'name', 'status', 'is_removed']



from .models import Persons

class PersonellerSerializer(serializers.ModelSerializer):
    personel_turu = PersonelTuruSerializer(read_only=True)
    personel_turu_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Persons
        fields = ['id', 'ad', 'soyad','unvan', 'personel_turu', 'personel_turu_id', 'img', 'durum', 'is_removed']

    def create(self, validated_data):
        personel_turu_id = validated_data.pop('personel_turu_id')
        personel_turu = PersonelTuru.objects.get(id=personel_turu_id)
        return Persons.objects.create(personel_turu=personel_turu, **validated_data)

    def update(self, instance, validated_data):
        personel_turu_id = validated_data.get('personel_turu_id', instance.personel_turu_id)
        personel_turu = PersonelTuru.objects.get(id=personel_turu_id)

        instance.ad = validated_data.get('ad', instance.ad)
        instance.soyad = validated_data.get('soyad', instance.soyad)
        instance.unvan = validated_data.get('unvan', instance.unvan)
        instance.personel_turu = personel_turu
        instance.img = validated_data.get('img', instance.img)
        instance.durum = validated_data.get('durum', instance.durum)
        instance.is_removed = validated_data.get('is_removed', instance.is_removed)

        instance.save()
        return instance





