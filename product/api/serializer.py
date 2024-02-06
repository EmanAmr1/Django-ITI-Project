from rest_framework import serializers
from category.models import *
from product.models import *


class Productserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())

   # def create(self,validated_data):
    #  pro=Product()
    # pro.name=validated_data['name']
    # pro.save()
    # return pro

    def create(self, validated_data):
        # ** means 3aml el validate data k dict
        return Product.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.category = validated_data.get('category')
        instance.category = validated_data.get('category')
        instance.save()
        return instance


     