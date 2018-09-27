from django.conf.urls import url
from .views import StoreApiView

urlpatterns = [
    url(r'state/$', StoreApiView.as_view(), name='StoreApiView'),
]
