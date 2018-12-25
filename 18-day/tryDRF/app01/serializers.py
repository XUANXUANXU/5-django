from rest_framework import serializers
from . import models


class PublisherSerializer(serializers.ModelSerializer):
    operator = serializers.ReadOnlyField(source='operator.username')
    class Meta:
        model = models.Publisher  # 我们要使用的模型
        # 我们要使用的字段
        fields = (
            'id',
            'name',
            'address',
            'operator'
        )

# 类名固定为表名称 + Serializer
# class PublisherSerializer(serializers.Serializer):
#     # read_only必须为True,因为我们模型里面的id是一个自增字段,不可写,自动生成
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#         # validated_data参数不需要特意去记,就是经过校验的数据
#         return models.Publisher.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.address = validated_data.get('address', instance.address)
#         instance.save()
#         return instance