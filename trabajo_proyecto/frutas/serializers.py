from rest_framework import serializers
from .models import Frutas


class FrutasSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    precio = serializers.IntegerField()
    stock = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)
        # valida los datos y crea una instancia del modelo en la base de datos
        return Frutas.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # En la función get recibimos 2 parámetros, el primero es la clave que se busca
        # en validated_data y el segundo parámetro sirve para que si no se proporciona un nuevo valor
        # este guardara el valor que ya estaba guardado en la base de datos
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.color = validated_data.get('color', instance.color)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance
