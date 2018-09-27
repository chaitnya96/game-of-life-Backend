# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import StoreApiSerializer
from django.core.exceptions import ValidationError
from .models import StoreApi

from rest_framework import generics


class StoreApiView(generics.ListCreateAPIView):
    queryset = StoreApi.objects.all()
    serializer_class = StoreApiSerializer
    permission_classes = (AllowAny,)


    # permission_classes = AllowAny
    #
    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     try:
    #         serializer = StoreApiSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return serializer.data
    #         else:
    #             raise ValidationError(serializer.errors,status.HTTP_404_NOT_FOUND)
    #         return Response(serializer, status.HTTP_201_CREATED)
    #     except ValidationError as e:
    #         return Response(e.errors, status=e.status)
    #
    # def get(self, request, *args, **kwargs):
    #     api = StoreApi.objects.all()
    #     serializer = StoreApiSerializer(api, many=True)
    #     self.permission_classes=AllowAny
    #     return Response(serializer.data)
