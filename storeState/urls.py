from django.conf.urls import url
from .views import StateListCreateAPIApiView, StateRetrieveUpdateDestroyApiView,DeleteAllState

urlpatterns = [
    url(r'^state/$', StateListCreateAPIApiView.as_view(), name='StateListCreateAPIApiView'),
    url(r'^state/(?P<pk>\d+)/$', StateRetrieveUpdateDestroyApiView.as_view(), name='StateRetrieveUpdateDestroyApiView'),
    url(r'^delete/$', DeleteAllState.as_view(), name='DeleteAllState'),
]
