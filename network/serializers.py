from rest_framework import serializers
from .models import NetworkNode, Contacts, Product


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt',)

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        products_data = validated_data.pop('products', [])

        contacts = Contacts.objects.create(**contacts_data)

        network_node = NetworkNode.objects.create(contacts=contacts, **validated_data)

        for product_data in products_data:
            product, _ = Product.objects.get_or_create(**product_data)
            network_node.products.add(product)

        return network_node


class NetworkNodeCreateSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer()

    class Meta:
        model = NetworkNode
        exclude = ('debt',)

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        contacts = Contacts.objects.create(**contacts_data)
        return NetworkNode.objects.create(contacts=contacts, **validated_data)
