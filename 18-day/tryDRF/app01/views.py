from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# from django.forms.models import model_to_dict
# from django.core import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from app01 import serializers
from .models import Publisher
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions


class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# class PublisherList(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     queryset = Publisher.objects.all()
#     serializers_class = serializers.PublisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PublisherDetail(mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       generics.GenericAPIView):
#
#     queryset = Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



# class PublisherList(APIView):
#     def get(self, request, format=None):
#         queryset = Publisher.objects.all()  # 查询出所有出版社
#         s = serializers.PublisherSerializer(queryset, many=True)
#         return Response(s.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         s = serializers.PublisherSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class PublisherDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Publisher.objects.get(pk=pk)
#         except Publisher.DoesNotExist:
#             raise Http404 # 需要先导入　
#
#     def get(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         s = serializers.PublisherSerializer(publisher)
#         return Response(s.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         s = serializers.PublisherSerializer(publisher, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         else:
#             Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         """删除出版社信息"""
#         publisher = self.get_object(pk)
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     # 查询出所有的出版社
#     if request.method == 'GET':
#         queryset = Publisher.objects.all()
#         s = serializers.PublisherSerializer(queryset,many=True)
#         return Response(s.data)
#     if request.method == 'POST':
#
#         s = serializers.PublisherSerializer(data=request.data)
#         if s.is_valid():  # 如果数据没问题
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def publisher_detail(request, pk):
#     try:
#             # 从数据库里面找你要找的pk
#         publisher = Publisher.objects.get(pk=pk)
#     except Publisher.DoesNotExist:  # 如果找不到浏览器传来的pk对应的数据,返回４０４
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#             # 从数据库里面取出来的publisher进行序列化
#         s = serializers.PublisherSerializer(publisher)
#         return Response(s.data)
#
#
#     if request.method == 'PUT':
#             # publisher使我们查出来的出版社信息　　request.data是客户端传过来的
#         s = serializers.PublisherSerializer(publisher, data=request.data)
#         if s.is_valid():  # 如果数据没有问题
#             s.save()
#             return Response(s.data)
#         else:
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     if request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

    # 转换成python中的列表
    # data = serializers.serialize('json',queryset)
    # for i in queryset:
    # data = []
    #     data.append(model_to_dict(i))
        # 每一个对象都手动转化成一个字典
        # p_tmp = {
        #     'name': i.name,
        #     'address': i.address
        # }
        # data.append(p_tmp)

    # import json
    #
    # return HttpResponse(json.dumps(s.data), content_type='application/json')