from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Slider
from .serializers import SliderSerializer
from rest_framework import status


from django.utils.translation import gettext as _
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_200_OK,
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken

from .authentication import token_expire_handler
from .serializers import AuthTokenSerializer,UsersSerializers
from django.contrib.auth.models import User


class ObtainExpiringAuthToken(ObtainAuthToken):  # Login
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            token = Token.objects.get(user=user)
            is_expired, token = token_expire_handler(token)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
        return Response({'token': token.key})


class VerifyToken(APIView):  # Check token expired or not
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get(self, request, format=None):
        return Response('', status=HTTP_200_OK)

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user         # request.user , ile istek atan kullanıcıya ulaşabilmek için bu servise token göndermek zorundasın
                                    # token göndermej için de kayıtlı bir kullanıcı olman lazım. önce tokenı veren servise istek atarsın
                                    # kayıtlı isen sana tokeni döndürür.
        serializer = UsersSerializers(user)
        return Response(serializer.data)



class SliderListView(ListAPIView):
    queryset = Slider.objects.filter(is_published=True)
    serializer_class = SliderSerializer


from rest_framework import viewsets
from .models import Menu, MenuItem
from .serializers import MenuSerializer, MenuItemSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = None
    def create(self, request, *args, **kwargs):
        selected = request.data.get('selected', False)

        # Eğer yeni menü seçili ise, diğer seçili menüyü bul ve selected değerini False yap
        if selected:
            try:
                existing_selected_menu = Menu.objects.get(selected=True)
                existing_selected_menu.selected = False
                existing_selected_menu.save()
            except Menu.DoesNotExist:
                pass  # Hiç seçili menü yok, devam et

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_update(self, serializer):
        # Yeni verilerden seçili değerini kontrol et
        selected = serializer.validated_data.get('selected', False)
        if selected:
            try:
                existing_selected_menu = Menu.objects.get(selected=True)
                if existing_selected_menu != serializer.instance:
                    # Güncellenecek menü, zaten seçili menü değilse
                    existing_selected_menu.selected = False
                    existing_selected_menu.save()
            except Menu.DoesNotExist:
                pass  # Hiç seçili menü yok, devam et

        serializer.save()

#class MenuItemViewSet(viewsets.ModelViewSet):
#    queryset = MenuItem.objects.all()
#    serializer_class = MenuItemSerializer

#    def retrieve(self, request, pk=None):
#        # Belirli bir menüye ait MenuItem nesnelerini getir
#        menu_items = MenuItem.objects.filter(menu_id=pk)
#        serializer = self.get_serializer(menu_items, many=True)
#       return Response(serializer.data)

from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer


# tüm menü ögelerini getirir
class MenuItemListCreateView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    pagination_class = None


# x menuye aıt menu ogelerini getir ve yeni öge üretir.
class MenuItemByMenuView(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer
    pagination_class = None

    def get_queryset(self):
        menu_id = self.kwargs.get('menu_id')
        return MenuItem.objects.filter(menu__id=menu_id)





# menu ogelerin her birinin tekil olarak detaylarını getir.
class MenuItemDetailView(generics.RetrieveUpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    pagination_class = None

# seçili menünün ögeleri listele
class MenuSelectedItemList(generics.ListAPIView):
    queryset = MenuItem.objects.filter(menu__selected=True,is_disabled=False)
    serializer_class = MenuItemSerializer
    #permission_classes = [IsAuthenticated]
    pagination_class = None






# Personeller
from .models import PersonelTuru
from .serializers import PersonelTuruSerializer
from rest_framework.decorators import action
class PersonelTuruViewSet(viewsets.ModelViewSet):
    queryset = PersonelTuru.objects.filter(is_removed=False).order_by('-id')
    serializer_class = PersonelTuruSerializer

    @action(detail=False, methods=['post'])
    def bulk_soft_delete(self, request):
        ids = request.data.get('ids', [])
        PersonelTuru.objects.filter(id__in=ids).update(is_removed=True)
        return Response(status=status.HTTP_204_NO_CONTENT)


from .models import Persons
from .serializers import PersonellerSerializer

class PersonellerViewSet(viewsets.ModelViewSet):
    queryset = Persons.objects.filter(is_removed=False).order_by('-id')
    serializer_class = PersonellerSerializer

    @action(detail=False, methods=['post'])
    def bulk_soft_delete(self, request):
        ids = request.data.get('ids', [])
        # Güvenli bir şekilde int listesi oluştur
        ids = [int(id) for id in ids if id.isdigit()]
        # Belirtilen ID'lere sahip nesneleri soft delete işlemi ile güncelle
        PersonelTuru.objects.filter(id__in=ids).update(is_removed=True)
        return Response(status=status.HTTP_204_NO_CONTENT)