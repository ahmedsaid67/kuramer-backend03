from django.urls import path,include
from .views import SliderListView, MenuViewSet, MenuItemListCreateView, MenuItemByMenuView, MenuItemDetailView, MenuSelectedItemList
from rest_framework.routers import DefaultRouter
from .views import ObtainExpiringAuthToken, VerifyToken, CurrentUserView
from .views import PersonelTuruViewSet,PersonellerViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'menus', MenuViewSet)

router_personel_turu = DefaultRouter()
router_personel_turu.register(r'personelturu', PersonelTuruViewSet)

router_personel = DefaultRouter()
router_personel.register(r'personeller', PersonellerViewSet)

urlpatterns = [
    # ...
    path('sliders/', SliderListView.as_view(), name='slider-list'),  # SliderListView'ı URL'ye ekleyin


    #menu apileri
    path('menu/', include(router.urls)),
    path('menuitems/', MenuItemListCreateView.as_view(), name='menuitem-list'),
    # Tüm nesneleri sunma için ve yeni öge üretmek
    path('menuitems/menu/<int:menu_id>/', MenuItemByMenuView.as_view(), name='menuitem-by-menu'),
    # Mkullanıcının isteği her hangi bir menünün ögelerini listeler
    path('menuitems/menu/selected/', MenuSelectedItemList.as_view(), name='menuitem-by-menu'),
    # seçili menünün ögeleri listeler
    path('menuitems/<int:pk>/', MenuItemDetailView.as_view(), name='menuitem-detail'),
    # Tekil menu öğelerini sunma için


    #personeller
    path('', include(router_personel_turu.urls)),
    path('', include(router_personel.urls)),

    #auth apileri
    path('token/login/', ObtainExpiringAuthToken.as_view()),
    path('token/verify/', VerifyToken.as_view()),
    path('auth/users/me/', CurrentUserView.as_view()),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)