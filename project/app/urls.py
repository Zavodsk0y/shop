from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path

from .views import *

urlpatterns = [
                  path('', ProductsListView.as_view(), name='products'),
                  path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
                  path('add-to-cart/<int:product_id>', add_to_cart, name='add-to-cart'),
                  path('profile', UserProfileView.as_view(), name='profile'),
                  path('create_product', ProductCreateView.as_view(), name='create_product'),
                  path('about', AboutTemplateView.as_view(), name='about'),
                  path('contacts', ContactsTemplateView.as_view(), name='contacts'),
                  path('login', LoginView.as_view(), name='login'),
                  path('logout', BBLogoutView.as_view(), name='logout')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
