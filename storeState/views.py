# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import StoreApi
from .serializers import StoreApiSerializer


class StateListCreateAPIApiView(generics.ListCreateAPIView):
    queryset = StoreApi.objects.all()
    serializer_class = StoreApiSerializer
    permission_classes = (AllowAny,)


class StateRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreApi.objects.all()
    serializer_class = StoreApiSerializer
    permission_classes = (AllowAny,)


class DeleteAllState(generics.DestroyAPIView):
    queryset = StoreApi.objects.all()
    serializer_class = StoreApiSerializer
    permission_classes = (AllowAny,)

    def delete(self, request, *args, **kwargs):
        return StoreApi.objects.all().delete()
