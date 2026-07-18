from rest_framework import serializers

from .models import (Address, Client, Category, 
                     Product, Transaction, TransactionItem)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class TransactionItemReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = TransactionItem
        fields = ["id", "product", "quantity"]


class TransactionItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionItem
        fields = ["product", "quantity"]


class TransactionReadSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    items = TransactionItemReadSerializer(many=True, read_only=True)

    class Meta:
        model = Transaction
        fields = ["id", "client", "created_at", "items"]


class TransactionWriteSerializer(serializers.ModelSerializer):
    items = TransactionItemWriteSerializer(many=True)

    class Meta:
        model = Transaction
        fields = ["client", "items"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")

        transaction = Transaction.objects.create(**validated_data)

        for item in items_data:
            TransactionItem.objects.create(
                transaction=transaction,
                **item
            )

        return transaction