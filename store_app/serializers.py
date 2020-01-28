from rest_framework import serializers
from store_app.models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=200)
    price = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)

        instance.save()
        return instance

    class Meta:
        model = Product
        fields = ['url','id', 'description', 'price']
