from rest_framework import serializers,exceptions
from .models import Slider
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        label=_("Username"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            # böyle bir kullanıcı var ise o kullanıcı nesnesi döner yoksa None döner.

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
            if not user.is_active:
                raise exceptions.AuthenticationFailed('Hesap aktif değil.')
            #if user.is_removed:
            #    raise exceptions.AuthenticationFailed('Hesap askıya alınmış.')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user  # geçici veri saklamaya yarar.
        return attrs


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







